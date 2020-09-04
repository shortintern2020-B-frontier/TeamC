from pydantic import BaseModel
from typing import Optional

class ChatCreate(BaseModel):
    user_id: int
    chat_room_id: int
    content: str
