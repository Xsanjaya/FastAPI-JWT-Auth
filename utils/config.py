from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
	SECRET 			: str
	ALGORITHM		: str
	DB_ENGINE 		: str
	DB_HOST			: str
	DB_PORT			: int
	DB_USER			: str
	DB_PASSWORD 	: str
	DB_NAME			: str
	DB_PATH			: str = "databases/"
	DB_POOL_SIZE 	: int = 20
	DB_POOL_PRE_PING	: bool = True
	DB_POOL_RECYCLE 	: int = 1800
	DB_ECHO 			: int = False

	class Config:
		env_file = '.env'

@lru_cache
def get_config():
	return Settings()


config = get_config()