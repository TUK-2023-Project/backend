import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SignLanguageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Initialize a variable to keep track of the total size of received video data
        self.total_size = 0

        while True:
            # Wait for 2 seconds
            await asyncio.sleep(2)

            # Send the total size to the front-end as a JSON message
            await self.send(text_data=json.dumps({
                'message': f'Total video data size: {self.total_size}'
            }))

    async def receive(self, text_data):
        # Get the video data from the front-end
        video_data = json.loads(text_data)

        # Increment the total size of the received video data
        self.total_size += len(video_data)

