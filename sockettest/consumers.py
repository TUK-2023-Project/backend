import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    #웹 소켓 연결혹은 연결 해제
    async def connect(self):
        print('연결됨')
        await self.accept()

    async def disconnect(self, close_code):
        print('해제됨')
        pass
    
    #메시지 받기
    def receive(self, text_data):
        #json으로 받기
        text_data_json=json.loads(text_data)
        message = text_data_json['message']
        print(message)

        #json객체 인코딩해서 보내기
        self.send(text_data=json.dumps({
            'message':message
        }))