# Author: Reika Kosuda
from pydantic import BaseModel
from typing import Optional
from typing import List

class ChatRoomCreate(BaseModel):
    guest_user_id: List[int]
