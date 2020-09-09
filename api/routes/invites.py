# Author:  Reika Kosuda
from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.users import users
from models.chat_rooms import chat_rooms
from models.user_chat_rooms import user_chat_rooms
from schemas.invites import *

from databases import Database

from utils.dbutils import get_connection
import time

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
@router.get("/invites/", response_model=List[InviteResponse])
async def invites_findall(user_id: str, database: Database = Depends(get_connection)):
    select_query = f"select * from user_chat_rooms where user_id = {user_id} and valid = 0"
    invites_data = await database.fetch_all(select_query)
    chat_rooms_ids = list(map(lambda n: n.chat_room_id, invites_data))
    if not chat_rooms_ids:
        user_invites = []
    else:
        select_query = f"select users.id, users.username, chat_room_id from user_chat_rooms left join users on user_chat_rooms.user_id = users.id where chat_room_id in ({','.join(map(str,chat_rooms_ids))}) and user_chat_rooms.user_id != {user_id}"
        user_datas = await database.fetch_all(select_query)
        user_invites = list(map(lambda n: {
            "id": n.id,
            "chat_room_id": str(n.chat_room_id),
            "users": list(filter(lambda p: p.chat_room_id == n.chat_room_id, user_datas))
        },
        invites_data))
    return user_invites

# user_chat_roomsのvalidを有効にしてchat_room_idを返します。
@router.post("/invites/agree", response_model=InviteSelect)
async def invite_agree(req: InviteAgree, database: Database = Depends(get_connection)):
    update_query = f"update user_chat_rooms set valid=1 where user_id = {req.user_id} and chat_room_id = {req.chat_room_id} and valid = 0"
    ret = await database.execute(update_query)
    #error定義　if ret == 0:
    select_query = f"select users.id, users.username from user_chat_rooms left join users on user_chat_rooms.user_id = users.id where user_chat_rooms.chat_room_id = {req.chat_room_id} and valid=1"
    user_datas = await database.fetch_all(select_query)
    chat_room_data = {
        "chat_room_id": str(req.chat_room_id),
        "users": user_datas
    }
    return chat_room_data

# Author:ZHANG CHI
# ユーザーAがBお誘いしましたの確認（フロントエンドのおすすめ部分使用）。
@router.post("/invites/recommend", response_model=List[InviteRecommend])
async def invites_recommend(invite:InviteCreate, database: Database = Depends(get_connection)):

    select_query = f"select valid, COUNT(DISTINCT valid)as count_valid from user_chat_rooms where chat_room_id IN (SELECT chat_room_id FROM user_chat_rooms WHERE user_id={invite.host_user_id}) AND chat_room_id IN (SELECT chat_room_id FROM user_chat_rooms WHERE user_id ={invite.guest_user_id})"
    invites_data = await database.fetch_all(select_query)
    return invites_data
