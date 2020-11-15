import json
import asyncio
from fastapi import APIRouter, Request, WebSocket
from fastapi.templating import Jinja2Templates

ws = APIRouter()
templates = Jinja2Templates(directory="templates")

with open('measurements.json', 'r') as file:
    measurements = iter(json.loads(file.read()))

@ws.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.htm", {"request": request})

@ws.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(0.1)
        payload = next(measurements)
        await websocket.send_json(payload)
