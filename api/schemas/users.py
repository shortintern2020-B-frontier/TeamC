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
    user_id: str
    username: str
    email: str
    password: str
    status: int
    comment: str

# select用のrequest model。selectでは、パスワード不要のため定義しない。
class UserSelect(BaseModel):
    user_id: str
    username: str
    email: str
    status: Optional[int] = 0
    comment: Optional[str] = ''
    status_update_at: Optional[str] = None
