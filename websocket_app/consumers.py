# C:\Users\user1\PycharmProjects\Telemetry-emulator\main\websocket_app\consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Process received data as needed
        response_data = {
            'message': 'Received data successfully',
            'data': data
        }
        await self.send(text_data=json.dumps(response_data))