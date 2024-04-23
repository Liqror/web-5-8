import firebase_admin
from firebase_admin import credentials, db

# Инициализация Firebase с использованием конфигурации
def initialize_firebase():
    firebase_config = {
        "apiKey": "AIzaSyCULB8i72nAIAqIP6sFS3HS4bK2gi48ckE",
        "authDomain": "chat-project-8f016.firebaseapp.com",
        "projectId": "chat-project-8f016",
        "storageBucket": "chat-project-8f016.appspot.com",
        "messagingSenderId": "664654209679",
        "appId": "1:664654209679:web:bcb0a44c9a423ac13b06fa",
        "measurementId": "G-MB4Z6G4G8Y"
    }
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred, {
       "databaseURL": "https://chat-project-8f016-default-rtdb.europe-west1.firebasedatabase.app/",  
    })

# Отправка сообщения в Firebase Realtime Database
def send_message_to_firebase(room_id, message):
    ref = db.reference(f'chat_rooms/{room_id}/messages')
    ref.push(message)

# Получение сообщений из Firebase Realtime Database
def get_messages_from_firebase(room_id):
    ref = db.reference(f'chat_rooms/{room_id}/messages')
    return ref.get()

