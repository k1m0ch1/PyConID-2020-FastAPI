from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from routes import root, piggybank, asynctest, ws
from flaskApp import flask_app
from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI()

app.include_router(root.root)
app.include_router(piggybank.account, prefix="/PiggyBank")
app.include_router(asynctest.asynctest, prefix="/AsyncTest")
app.include_router(ws.ws, prefix="/WebSocket")

app.mount('/v1', WSGIMiddleware(flask_app.app))
