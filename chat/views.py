# chat/views.py
from django.shortcuts import render, get_object_or_404
from .models import ChatRoom
from django.shortcuts import render
from .models import ChatRoom
from django.shortcuts import render, redirect
from .models import ChatRoom
from .forms import CreateRoomForm


def room_detail(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
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