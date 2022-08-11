import email
from email import message
from lib2to3.pgen2 import token
from fastapi import FastAPI
from pydantic import BaseModel
from Models.user import User
from Auth.jwt_handler import signJWT, decodeJWT

from utils.db import engine
from sqlalchemy.orm import Session

user_route = FastAPI()

class UserValidator(BaseModel):
    name  : str
    email : str
    password : str 

class TokenValidator(BaseModel):
    token  : str


@user_route.post('/users/create')
async def create(request : UserValidator):
    name =  request.name
    email = request.email
    password =  request.password

    try:
        with Session(engine) as mydb:
            user = User(name=name, email=email, password=password, token=signJWT(email) )
            mydb.add( user )
            mydb.commit()
            
            result = {
            'name' : name,
            'email' : email,
            'token' : signJWT(email)
            }

    except Exception as e:
        print(e)
        result = {
            "message" : e
        }
    
    return result

@user_route.post('/users/login')
async def login(request : TokenValidator):
    token =  request.token

    result = {
        'token' : decodeJWT(token)
    }
    return result
