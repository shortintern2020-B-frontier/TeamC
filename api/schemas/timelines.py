# Author: Reika Kosuda
from pydantic import BaseModel
from typing import Optional

class TimeLineCreate(BaseModel):
    user_id: int
    event_date: int
    place: str
    content: str

class TimeLineUpdate(BaseModel):
    id: int
    user_id: int
    event_date: Optional[int] = None
    place: Optional[str] = None
    content: Optional[str] = None

class TimeLineJoin(BaseModel):
    id: int
    user_id: int
