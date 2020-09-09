# Author hirata
from pydantic import BaseModel
from typing import Optional

class ChatCreate(BaseModel):
    user_id: int
    chat_room_id: int
    content: str

class ChatDetail(BaseModel):
    id: int
    user_id: int
    created_at: Optional[str] = None
    content: str
    username: str