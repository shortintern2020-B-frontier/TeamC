# Author: Reika Kosuda

from pydantic import BaseModel
from typing import Optional

# insert用のrequest model
class InviteCreate(BaseModel):
    id: int
    user_1_id: int
    user_2_id: int
