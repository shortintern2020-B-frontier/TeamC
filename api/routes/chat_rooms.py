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

# Author hirata
# Get ChatRooms
@router.get("/chat_rooms/")
async def get_chat_room(id: int, database: Database = Depends(get_connection)):
    select_room_query = f"select * from chat_rooms left join user_chat_rooms on chat_rooms.id = user_chat_rooms.chat_room_id where user_chat_rooms.user_id = {id} and user_chat_rooms.valid = 1 order by chat_rooms.id desc"
    chat_rooms = await database.fetch_all(select_room_query)
    chat_rooms = list(map(lambda n: dict(n), chat_rooms))
    chat_room_ids = list(map(lambda n: n['id'], chat_rooms))
    if not chat_room_ids:
        return []
    select_chat_query = f"select * from chats where id in ( select max(id) from chats where chat_room_id in ({','.join(map(str, chat_room_ids))}) group by chat_room_id)"
    chats = await database.fetch_all(select_chat_query)
    chats = list(map(lambda n: dict(n), chats))
    for chat_room in chat_rooms:
        chats_of_the_room = list(filter(lambda n: n['chat_room_id'] == chat_room['id'], chats))
        if chats_of_the_room:
            chat_room['last_chat'] = chats_of_the_room[0]
    user_select_query = f"select users.id, users.username, chat_room_id from user_chat_rooms left join users on user_chat_rooms.user_id = users.id where chat_room_id in ({','.join(map(str,chat_room_ids))}) and user_chat_rooms.user_id != {id} and user_chat_rooms.valid = 1"
    user_datas = await database.fetch_all(user_select_query)
    for chat_room in chat_rooms:
        chat_room['users'] = list(filter(lambda p: p.chat_room_id == chat_room['id'], user_datas))
    return chat_rooms