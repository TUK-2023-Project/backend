import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SignLanguageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Initialize a variable to keep track of the total size of received video data
        self.total_size = 0

      

    async def receive(self, text_data):
        # Get the video data from the front-end
        video_data = json.loads(text_data)

  
        landmarks = []

        for item in video_data['message']:
            for sub_item in item:
                 if isinstance(sub_item, dict):
                    landmarks.append({"landmarks": sub_item['landmarks']})

        print(landmarks)
        
        
        # landmarks 데이터 AI처리
        # AI처리된 결과를 return하기



        await self.send(text_data=json.dumps({
            'message': 'Data received successfully'
        }))

