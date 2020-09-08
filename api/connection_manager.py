# Author hirata
from typing import List, Dict
from collections import defaultdict
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connection_dict: Dict[int, List[WebSocket]] = defaultdict(list)

    async def connect(self, room_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connection_dict[room_id].append(websocket)

    def disconnect(self, room_id: int, websocket: WebSocket):
        self.active_connection_dict[room_id].remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, room_id: int, message: str):
        for connection in self.active_connection_dict[room_id]:
            await connection.send_text(message)