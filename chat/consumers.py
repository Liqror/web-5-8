# chat/consumers.py
import json
from .firebase_utils import initialize_firebase, send_message_to_firebase, get_messages_from_firebase

# Инициализация Firebase
initialize_firebase()

class ChatConsumer:
    async def connect(self):
        # Получаем room_id из URL
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        # Формируем имя группы комнаты
        self.room_group_name = f'chat_{self.room_id}'

        # Принимаем WebSocket-соединение
        await self.accept()

    async def disconnect(self, close_code):
        # Покидаем группу комнаты при отключении
        pass

    async def receive(self, text_data):
        # Десериализуем JSON-данные
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправляем сообщение в Firebase Realtime Database
        send_message_to_firebase(self.room_id, message)

        # Отправляем сообщение в группу комнаты
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Получаем сообщение из группы комнаты
    async def chat_message(self, event):
        message = event['message']

        # Отправляем сообщение по WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
