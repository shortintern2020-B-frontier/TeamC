# Author: Reika Kosuda
from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.users import users
from models.friends import friends
from models.chat_rooms import chat_rooms
from models.user_chat_rooms import user_chat_rooms
from models.timelines import timelines
from schemas.users import *
from schemas.timelines import *

from databases import Database

from utils.dbutils import get_connection

#from datetime import datetime

router = APIRouter()

# timelinesを新規登録します。
@router.post("/timelines/", response_model=TimeLineUpdate)
async def timelines_create(timeline: TimeLineCreate, database: Database = Depends(get_connection)):
    insert_query = timelines.insert()
    values = timeline.dict()
    values["deleted"] = 0
    ret = await database.execute(insert_query, values)
    select_query = f"select id from timelines where user_id = {timeline.user_id} order by id desc limit 1"
    timeline_data = await database.fetch_one(select_query)
    values.pop("deleted")
    values["id"] = getattr(timeline_data, "id")
    return values

# 自分とfrends_idに紐づいているtimelineの情報を返す
@router.get("/timelines/", response_model=List[TimeLineUpdate])
async def timelines_findall(user_id: int, database: Database = Depends(get_connection)):
    select_query = f"select timelines.id, timelines.user_id, timelines.event_date, timelines.place, timelines.content from timelines left join friends on timelines.user_id = friends.user_1_id where timelines.deleted = 0 and (timelines.user_id={user_id} or friends.user_2_id = {user_id})"
    return await database.fetch_all(select_query)

# timeline参加希望者からchat_roomへのinviteを生成
@router.post("/timelines/join")
async def timeline_join(req: TimeLineJoin, database: Database = Depends(get_connection)):
    # chat へのinvite
    select_query = f"select timelines.user_id from timelines where timelines.id = {req.id}"
    timeline_data = await database.fetch_one(select_query)
    insert_query = chat_rooms.insert()
    values = {
        "deleted":0
    }
    ret = await database.execute(insert_query, values)
    select_query = "select * from chat_rooms order by id desc limit 1"
    chat_room_data = await database.fetch_one(select_query)
    query = user_chat_rooms.insert()
    values1 = {
        "user_id": req.user_id,
        "chat_room_id": getattr(chat_room_data, "id"),
        "valid": 1
    }
    values2 = {
        "user_id": getattr(timeline_data, "user_id"),
        "chat_room_id": getattr(chat_room_data, "id"),
        "valid": 0
    }
    await database.execute(query, values1)
    await database.execute(query, values2)
    return {"result":"join success"}

# timelinesを更新します。
@router.post("/timelines/update", response_model=TimeLineUpdate)
async def timeline_update(timeline: TimeLineUpdate, database: Database = Depends(get_connection)):
    select_query = f"select * from timelines where id = {timeline.id} and user_id = {timeline.user_id}"
    timeline_data = await database.fetch_one(select_query)
    if timeline_data is None:
        return None
    update_query = timelines.update().where(timelines.columns.id==timeline.id)
    for k, v in dict(timeline).items():
        if v == None and hasattr(timeline_data, k):
            setattr(timeline, k, getattr(timeline_data, k))
    values = dict(timeline)
    ret = await database.execute(update_query, values)
    return values

# timelinesを削除します。
@router.post("/timelines/delete")
async def timelines_delete(timeline: TimeLineJoin, database: Database = Depends(get_connection)):
    query = f"delete from timelines where id = {timeline.id} and user_id={timeline.user_id})"
    ret = await database.execute(query)
    return {"result":"delete success"}
