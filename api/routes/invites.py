# Author:  Reika Kosuda
from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.chat_rooms import chat_rooms
from models.user_chat_rooms import user_chat_rooms
from schemas.invites import *

from databases import Database

from utils.dbutils import get_connection

router = APIRouter()

# inviteを生成します。
@router.post("/invites/create")
async def invite_create(invite: InviteCreate, database: Database = Depends(get_connection)):
    insert_query = chat_rooms.insert()
    values = {
        "deleted":0
    }
    await database.execute(insert_query, values)
    select_query = "select * from chat_rooms order by id desc limit 1"
    chat_room_data = await database.fetch_one(select_query)
    chat_room_id = getattr(chat_room_data, "id")
    query = user_chat_rooms.insert()
    values1 = {
        "user_id": invite.host_user_id,
        "chat_room_id": chat_room_id,
        "valid": 1
    }
    values2 = {
        "user_id": invite.guest_user_id,
        "chat_room_id": chat_room_id,
        "valid": 0
    }
    await database.execute(query, values1)
    await database.execute(query, values2)
    return {"result":"invite success"}

# お誘い一覧を返します。
@router.get("/invites")
async def invites_findall(user_id: str, database: Database = Depends(get_connection)):
    select_query = f"select * from user_chat_rooms where user_id = {user_id} and valid = 0"
    invites_data = await database.fetch_all(select_query)
    user_invites = []
    for item in invites_data:
        chat_room_id = getattr(item, "chat_room_id")
        select_query = f"select * from user_chat_rooms where chat_room_id = {chat_room_id} and valid = 1 and user_id != {user_id}"
        host_user_data = await database.fetch_one(select_query)
        values = {
            "host_user_id": str(getattr(host_user_data, "user_id")),
            "guest_user_id": user_id,
            "chat_room_id": str(chat_room_id)
        }
        user_invites.append(values)
    return user_invites
