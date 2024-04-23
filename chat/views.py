# chat/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateRoomForm
from .models import ChatRoom, Message
from django.http import JsonResponse
import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def room_detail(request, room_id):  # Измените параметр на room_id
    room = get_object_or_404(ChatRoom, id=room_id)  # Используйте room_id для получения комнаты
    return render(request, 'chat/room_detail.html', {'room': room})

def chat_list(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/chat_list.html', {'chat_rooms': chat_rooms})

def create_room(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            # Вывод отладочной информации о полученных данный из формы
            print(form.cleaned_data)
            # Сохранение формы в базе данных
            form.save()
            # Перенаправление на страницу списка чатов
            return redirect('chat_list')
    else:
        form = CreateRoomForm()
    return render(request, 'chat/create_room.html', {'form': form})


def send_message(request, room_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        room = ChatRoom.objects.get(id=room_id)
        message = Message.objects.create(room=room, sender=sender, content=content)
        
        # Отправить сообщение через WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"chat_{room_id}",
            {
                "type": "chat.message",
                "message": {
                    "sender": sender.username,
                    "content": content,
                    "timestamp": message.timestamp.isoformat(),
                },
            },
        )
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



def get_messages(request, room_id):
    if request.method == 'GET':
        room = ChatRoom.objects.get(id=room_id)
        messages = room.messages.all()
        data = [{'sender': msg.sender.username, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages]
        return JsonResponse({'messages': data})