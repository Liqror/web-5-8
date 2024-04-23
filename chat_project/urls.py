# chat_project/urls.py
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from chat.views import chat_list, room_detail  # Импортируем представление chat_list
from django.shortcuts import redirect  # Импортируем функцию redirect
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView
from django.shortcuts import redirect  # Импортируем функцию redirect


urlpatterns = [
    path('', lambda request: redirect('chat_list')),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # Подключаем URL-адреса чата
]