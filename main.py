from fastapi import FastAPI
from Routes import user_route, user_route2, web_route

app = FastAPI()
app.mount('/api/v1/', user_route)
app.mount('/api/v2/', user_route2)
app.mount('/', web_route)


