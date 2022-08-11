import email
from unicodedata import name
from fastapi import FastAPI, Depends, HTTPException
from Auth.auth_handler import AuthHandler
from pydantic import BaseModel
from Models import user
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
            raise HTTPException(status_code=400, detail='Email is taken')
        hashed_password = auth_handler.get_password_hash(request.password)
        user = mydb.add(User(name=request.name, email=request.email, password=hashed_password))
        mydb.commit()
    return   
     


@user_route2.post('/users/login')
def login(request: UserValidator):
    user = None
    for x in users:
        if x['username'] == request.username:
            user = x
            break
    
    if (user is None) or (not auth_handler.verify_password(request.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return { 'token': token }


@user_route2.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }


@user_route2.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }