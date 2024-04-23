# chat/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_room, name='create_room'),  # URL для создания комнаты
    path('', views.chat_list, name='chat_list'),  # Список всех комнат
    path('<int:room_id>/', views.room_detail, name='room_detail'),  # Детали конкретной комнаты
    path('<int:room_id>/send_message/', views.send_message, name='send_message'),
    path('<int:room_id>/get_messages/', views.get_messages, name='get_messages'),
]