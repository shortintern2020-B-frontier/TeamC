# Author hirata
import hashlib

from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.chats import chats
from schemas.chats import *

from databases import Database

from utils.dbutils import get_connection
import time
from datetime import datetime

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
@router.get("/chats/", response_model=List[ChatDetail])
async def get_chat(chat_room_id: int, database: Database = Depends(get_connection)):
    # validatorは省略
    query = f'select chats.id, chats.content as content, chats.created_at as created_at, chats.user_id as user_id, users.username as username from chats left join users on chats.user_id = users.id where chats.chat_room_id = {chat_room_id} order by chats.id'
    chats = await database.fetch_all(query)
    chats = list(map(lambda n: dict(n), chats))
    for chat in chats:
      if chat['created_at']:
        chat['created_at'] = datetime.fromtimestamp(chat['created_at']).strftime('%Y/%m/%d %H:%M')
    return chats