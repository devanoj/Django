# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_box_view, name='chat_box'),
    path('voice/', views.create_text_v)
]