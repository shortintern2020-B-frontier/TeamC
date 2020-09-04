import hashlib

from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.chats import chats
from schemas.chats import *

from databases import Database

from utils.dbutils import get_connection
import time

router = APIRouter()

# Create Chat
@router.post("/chats/", response_model=ChatCreate)
async def create_chat(req: ChatCreate, database: Database = Depends(get_connection)):
    # validatorは省略
    query = chats.insert()
    values = req.dict()
    values['created_at'] = int(time.time())
    ret = await database.execute(query, values)
    return {**req.dict()}

# Get Chat
@router.get("/chats/", response_model=List[ChatCreate])
async def get_chat(chat_room_id: int, database: Database = Depends(get_connection)):
    # validatorは省略
    query = chats.select().where(chats.columns.chat_room_id==chat_room_id)
    return await database.fetch_all(query)