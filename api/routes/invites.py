# Author:  Reika Kosuda
from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.invites import chat_rooms, user_chat_rooms
from schemas.invites import *

from databases import Database

from utils.dbutils import get_connection

router = APIRouter()

# 誘う
#   ->誘う側:ユーザチャットルーム valid=Trueで開く
#   ->誘われる側:ユーザチャットルーム　valid=Falseで開く

# inviteを生成します。
@router.post("/invites/create")
async def invite_create(invite: InviteCreate, database: Database = Depends(get_connection)):
    # chat_roomsを一つ生成
    query = chat_rooms.insert()
    values = {
        "deleted":0
    }
    await database.execute(query, values)
    # 作成したchat_roomのidを取得
    select_query = "select * from chat_rooms order by id desc limit 1"
    chat_room_data = await database.fetch_one(select_query)
    chat_room_id = getattr(chat_room_data, "id")
    # user_chat_rooms(関連)を2つ生成：valid=1, valid=0
    query = user_chat_rooms.insert()
    values1 = {
        "user_id": invite.user_1_id,
        "chat_room_id": chat_room_id,
        "valid": 1
    }
    values2 = {
        "user_id": invite.user_2_id,
        "chat_room_id": chat_room_id,
        "valid": 0
    }
    await database.execute(query, values1)
    await database.execute(query, values2)
    return {"result":"invite success"}
