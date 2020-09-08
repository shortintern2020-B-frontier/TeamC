# Author:  Reika Kosuda
from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.users import users
from models.chat_rooms import chat_rooms
from models.user_chat_rooms import user_chat_rooms
from schemas.chat_rooms import *
from schemas.invites import InviteSelect

from databases import Database

from utils.dbutils import get_connection

router = APIRouter()

# Create Chat_room
@router.post("/chat_rooms/")
async def create_chat_room(req: ChatRoomCreate, database: Database = Depends(get_connection)):
    #values = ','.join(['(0)' for n in range(len(req.guest_user_id))])
    #insert_query = f"insert chat_rooms (deleted) values {values}"
    insert_query = chat_rooms.insert()
    values = {
        "deleted": 0
    }
    await database.execute(insert_query, values)
    select_query = f"select * from chat_rooms order by id desc limit 1"
    chat_room = await database.fetch_one(select_query)
    chat_room_id = getattr(chat_room, "id")
    values = ','.join(['('+ str(user_id) + ',' + str(chat_room_id) +', 0)' for user_id in req.guest_user_id])
    insert_query = f"insert user_chat_rooms (user_id, chat_room_id, valid) values {values}"
    await database.execute(insert_query)

    select_query = f"select users.id, users.username, user_chat_rooms.valid from user_chat_rooms left join users on user_chat_rooms.user_id = users.id where user_chat_rooms.chat_room_id = {chat_room_id}"
    #select_query = f"select users.id, users.username from user_chat_rooms left join users on user_chat_rooms.user_id = users.id where user_chat_rooms.chat_room_id = {req.chat_room_id} and valid=1"
    user_datas = await database.fetch_all(select_query)
    chat_room_data = {
        "chat_room_id": str(chat_room_id),
        "users": user_datas
    }
    return chat_room_data
