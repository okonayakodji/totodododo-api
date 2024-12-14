from fastapi import FastAPI, APIRouter

from user import user

app = FastAPI()

api = APIRouter()


@api.get("/hi")
async def get_hi():
    return "Hi"


api.include_router(user, prefix="/user")
app.include_router(api, prefix="/api")
