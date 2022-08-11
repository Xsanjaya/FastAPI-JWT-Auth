from fastapi import FastAPI
from Routes import user_route

app = FastAPI()
app.mount('/api/v1/', user_route)


