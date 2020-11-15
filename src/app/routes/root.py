from fastapi import APIRouter

root = APIRouter()

@root.get("/")
async def index():
    return {"message": "Hello World"}


@root.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
