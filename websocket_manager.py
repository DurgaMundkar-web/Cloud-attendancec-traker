from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        # सर्व ऑनलाईन युजर्सच्या एक्टिव्ह कनेक्शन्सची लिस्ट
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        # सर्व कनेक्टेड युजर्सना मेसेज पाठवा
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()