from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from db import database
from routes.users import router as userrouter
from routes.chats import router as chatrouter
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
from connection_manager import ConnectionManager
import json

app = FastAPI()
manager = ConnectionManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 起動時にDatabaseに接続する。
@app.on_event("startup")
async def startup():
    await database.connect()

# 終了時にDatabaseを切断する。
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# users routerを登録する。
app.include_router(userrouter)
app.include_router(chatrouter)

# middleware state.connectionにdatabaseオブジェクトをセットする。
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int):
    # Todo: add filter for subscribers
    await manager.connect(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(room_id, data)
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
