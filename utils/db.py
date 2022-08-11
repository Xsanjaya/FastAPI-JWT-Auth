import sqlalchemy as sa, os
from utils.config import config

DB_ENGINE = config.DB_ENGINE.lower()
if DB_ENGINE in ['mysql', 'postgress', 'oracle']:
	DB = f"{config.DB_ENGINE}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
	engine = sa.create_engine(
		DB,
		pool_size 		= config.DB_POOL_SIZE,
		pool_pre_ping 	= config.DB_POOL_PRE_PING,
		pool_recycle 	= config.DB_POOL_RECYCLE,
		echo 			= config.DB_ECHO
		)

elif DB_ENGINE =='sqlite3':
	DB = f"sqlite:///{config.DB_NAME}"
	engine = sa.create_engine(
		DB,
		pool_pre_ping 	= config.DB_POOL_PRE_PING,
		pool_recycle 	= config.DB_POOL_RECYCLE,
		echo 			= config.DB_ECHO
		)
