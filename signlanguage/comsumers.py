import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from AI import predict

class SignLanguageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
  

      
    async def receive(self, text_data):
        video_data = json.loads(text_data)

  
        landmarks = []

        for item in video_data['message']:
            for sub_item in item:
                 if isinstance(sub_item, dict):
                    landmarks.append({"landmarks": sub_item['landmarks']})


        await self.send(text_data=json.dumps({
            'message': predict.run(landmarks)
        }))

