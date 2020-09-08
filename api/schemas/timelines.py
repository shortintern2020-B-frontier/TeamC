# Author: Reika Kosuda
from pydantic import BaseModel
from typing import Optional

class TimeLineCreate(BaseModel):
    user_id: int
    event_date: int
    place: str
    content: str

class TimeLineSelect(BaseModel):
    id: int
    user_id: int
    event_date: int
    place: str
    content: str

class TimeLineJoin(BaseModel):
    id: int
    user_id: int
