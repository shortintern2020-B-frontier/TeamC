# Author: Reika Kosuda
from pydantic import BaseModel
from typing import Optional

# insert用のrequest model
class InviteCreate(BaseModel):
    host_user_id: int
    guest_user_id: int

class InviteSelect(BaseModel):
    chat_room_id: str
    users: list

class InviteResponse(BaseModel):
    id: int
    chat_room_id: str
    users: list

class InviteAgree(BaseModel):
    user_id: str
    chat_room_id: int
