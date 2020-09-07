# Author: Reika Kosuda
from pydantic import BaseModel
from typing import Optional

# insert用のrequest model
class InviteCreate(BaseModel):
    host_user_id: int
    guest_user_id: int
    chat_room_id: Optional[int] = None
