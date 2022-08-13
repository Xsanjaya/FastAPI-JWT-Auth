from unittest import result
from fastapi import FastAPI

web_route = FastAPI()

@web_route.get('/')
async def index():
    result = {
        'message' : 'API RUNING'
    }

    return result