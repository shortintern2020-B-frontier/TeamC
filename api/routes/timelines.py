# Author: Reika Kosuda
from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.users import users
from models.friends import friends
from models.timelines import timelines
from schemas.users import *
from schemas.timelines import *

from databases import Database

from utils.dbutils import get_connection

#from datetime import datetime

router = APIRouter()

# timelinesを新規登録します。
@router.post("/timelines/", response_model=TimeLineSelect)
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

# frends_idに紐づいているtimelineの情報を返す
@router.get("/timelines/", response_model=List[TimeLineSelect])
async def timelines_findall(user_id: int, database: Database = Depends(get_connection)):
    select_query = f"select timelines.id, timelines.user_id, timelines.event_date, timelines.place, timelines.content from timelines left join friends on timelines.user_id = friends.user_1_id where friends.user_2_id = {user_id}"
    return await database.fetch_all(select_query)

# timeline 参加
#@router.post("/timelines/join")
#async def timeline_join(req: TimeLineJoin, database: Database = Depends(get_connection)):


# timelinesを更新します。
#@router.post("/timelines/update")

## timelineへのchatsを追加します。

# timelinesを削除します。
