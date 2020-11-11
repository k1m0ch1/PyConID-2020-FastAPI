from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_main():
    return {"message": "Hello"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 210
    assert response.json() == {"message": "Hello"}

test_read_main()
