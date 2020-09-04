import hashlib

from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from models.users import users
from models.friends import friends
from schemas.users import *

from databases import Database

from utils.dbutils import get_connection

router = APIRouter()

# 入力したパスワード（平文）をハッシュ化して返します。
def get_users_insert_dict(user):
    pwhash=hashlib.sha256(user.password.encode('utf-8')).hexdigest()
    values=user.dict()
    values.pop("password")
    values["hashed_password"]=pwhash
    return values

# usersを全件検索して「UserSelect」のリストをjsonにして返します。
@router.get("/users/", response_model=List[UserSelect])
async def users_findall(request: Request, database: Database = Depends(get_connection)):
    query = users.select()
    return await database.fetch_all(query)

# usersをidで検索して「UserSelect」をjsonにして返します。
@router.get("/users/find", response_model=UserSelect)
async def users_findone(user_id: str, database: Database = Depends(get_connection)):
    query = users.select().where(users.columns.user_id==user_id)
    return await database.fetch_one(query)

@router.post("/users/login", response_model=UserSelect)
async def login_user(req: RequestForLogin, database: Database = Depends(get_connection)):
    query = users.select().where(users.columns.email==req.email)
    return await database.fetch_one(query)

@router.post("/users/friends")
async def make_friends(req: RequestForMakeFriends, database: Database = Depends(get_connection)):
    query = users.select().where(users.columns.id==req.user_id)
    user1 = await database.fetch_one(query)
    query = users.select().where(users.columns.id==req.target_user_id)
    user2 = await database.fetch_one(query)
    query = friends.insert()
    values1 = {
        "user_1_id": user1.id,
        "user_2_id": user2.id
    }
    values2 = {
        "user_1_id": user2.id,
        "user_2_id": user1.id
    }
    await database.execute(query, values1)
    await database.execute(query, values2)
    return {"result": "connect success"}

# usersを新規登録します。
@router.post("/users/create", response_model=UserSelect)
async def users_create(user: UserCreate, database: Database = Depends(get_connection)):
    # validatorは省略
    query = users.insert()
    values = get_users_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}

# usersを更新します。
@router.post("/users/update", response_model=UserSelect)
async def users_update(user: UserUpdate, database: Database = Depends(get_connection)):
    # validatorは省略
    query = users.update().where(users.columns.id==user.id)
    values=get_users_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}

# usersを削除します。
@router.post("/users/delete")
async def users_delete(user: UserUpdate, database: Database = Depends(get_connection)):
    query = users.delete().where(users.columns.id==user.id)
    ret = await database.execute(query)
    return {"result": "delete success"}
