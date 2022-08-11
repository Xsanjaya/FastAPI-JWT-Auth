from lib2to3.pgen2 import token
from Models import Base
import sqlalchemy as sa 

class User(Base):
    __tablename__ = 'users'

    id 			= sa.Column('id', sa.Integer, primary_key=True)
    name		= sa.Column('name', sa.String)
    email		= sa.Column('email', sa.String, unique=True)
    password	= sa.Column('password', sa.String)
    token       = sa.Column('token', sa.String)
    created_at 	= sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    updated_at 	= sa.Column('updated_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())