from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
	'''Get the Item ID and return the Item ID'''
	return {"item_id": item_id}
