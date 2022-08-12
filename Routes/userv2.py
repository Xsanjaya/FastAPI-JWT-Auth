from fastapi import FastAPI, Depends, HTTPException
from Auth.auth_handler import AuthHandler
from pydantic import BaseModel
from Models.user import User

from utils.db import engine
from sqlalchemy.orm import Session

user_route2 = FastAPI()

auth_handler = AuthHandler()
users = []

class UserValidator(BaseModel):
    name  : str
    email : str
    password : str 

@user_route2.post('/users/create', status_code=201)
def register(request: UserValidator):
    with Session(engine) as mydb:
        if mydb.query(User).filter(User.email == request.email).first() != None:
            result = { 
                "success" : False,
                "message" : "Email is taken",
                "data"    : None
            }
            raise HTTPException(status_code=400, detail=result)
        hashed_password = auth_handler.get_password_hash(request.password)
        user = mydb.add(User(name=request.name, email=request.email, password=hashed_password))
        mydb.commit()
        result = {
            "success" : True,
            "message" : "Create User Success",
            "data"    : {
                "name" : request.name,
                "email" : request.email
            }
        }
    return result
     


@user_route2.post('/users/login')
def login(request: UserValidator):
    with Session(engine) as mydb:
        user =  mydb.query(User).filter(User.email == request.email).first()
        if (user is None) or (not auth_handler.verify_password(request.password, user.password)):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
        token = auth_handler.encode_token(user.email)
    return { 'token': token }


@user_route2.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }