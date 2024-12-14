from fastapi import APIRouter

user = APIRouter()


@user.get("/{id}")
async def get_user(id):
    return f"Some user {id}"
