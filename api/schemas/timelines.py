# Author: Reika Kosuda
from pydantic import BaseModel
from typing import Optional

class TimeLineCreate(BaseModel):
    user_id: int
    event_date: int
    place: str
    content: str
