import json
from channels.generic.websocket import AsyncWebsocketConsumer
from AI import predict

class SignLanguageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        media_pipe = data['message']
        category_id = data.get('categoryId', 1)

        if category_id == 3:
   
            parsedData = {'left': [], 'right': []}

            for data in media_pipe:
                left_list = []
                right_list = []

                for point in data['left']:
                    left_list.extend([point['x'], point['y'], point['z']])

                for point in data['right']:
                    right_list.extend([point['x'], point['y'], point['z']])

                parsedData['left'].append(left_list)
                parsedData['right'].append(right_list)

            result = predict.run(parsedData, category_id)
    
            await self.send(text_data=json.dumps({
                'message': result
            }))

        else:

            landmarks = []
            for item in media_pipe:
                for sub_item in item:
                    if isinstance(sub_item, dict):
                        landmarks.append({"landmarks": sub_item['landmarks']})


            result = predict.run(landmarks, category_id)
    
            await self.send(text_data=json.dumps({
                'message': result
            }))
