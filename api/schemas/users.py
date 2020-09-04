from pydantic import BaseModel
from typing import Optional

# insert用のrequest model。id(自動採番)は入力不要のため定義しない。
class UserCreate(BaseModel):
    username: str
    user_id: str
    email: str
    password: str
    status: Optional[int] = 0
    comment: Optional[str] = ''

# update用のrequest model
class UserUpdate(BaseModel):
    id : int
    user_id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    status: Optional[int] = None
    comment: Optional[str] = None

# select用のrequest model。selectでは、パスワード不要のため定義しない。
class UserSelect(BaseModel):
    user_id: str
    username: str
    email: str
    status: Optional[int] = 0
    comment: Optional[str] = ''
    status_update_at: Optional[str] = None

class RequestForLogin(BaseModel):
    email: str
    password: str

class RequestForMakeFriends(BaseModel):
    user_id: int
    target_user_id: int