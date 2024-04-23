# chat/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_room, name='create_room'),  # URL для создания комнаты
    path('', views.chat_list, name='chat_list'),  # Список всех комнат
    path('<str:room_name>/', views.room_detail, name='room_detail'),  # Детали конкретной комнаты
]