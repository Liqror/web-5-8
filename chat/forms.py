from django import forms
from .models import ChatRoom

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'description']  # Укажите здесь поля, которые вы хотите включить в форму
