from typing import Optional
from fastapi import APIRouter, Query
from pydantic import BaseModel

account = APIRouter()

PiggyBank = []

class Account(BaseModel):
	index: int = None
	name: str
	date: str
	description: Optional[str] = None
	price: float
	category: Optional[str]

@account.get("/")
async def get_piggy_bank(start: int=0, end: int=Query(10, ge=0)):
	return PiggyBank[start:end]

@account.post("/saving")
async def post_saving(data: Account):
	data.category = 'saving'
	data.index = len(PiggyBank)+1
	PiggyBank.append(data.dict())
	return {"data": data.dict(), "message": "new saving is saved"}

@account.post("/expense")
async def post_expense(data: Account):
	data['category'] = 'expense'
	data.index = len(PiggyBank)+1
	PiggyBank.append(data.dict())
	return {"data": data.dict(), "message": "new expense is saved"}
