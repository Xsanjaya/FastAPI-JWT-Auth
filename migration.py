from utils.db import engine
from Models import Base
from Models.user import User

def create_table():
	User()
	return Base.metadata.create_all(engine)


create_table()