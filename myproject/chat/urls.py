# chat/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/', views.chat_box_view, name='chat_box'),
    path('email/<str:email>/', views.email_view, name='email_view'),
    # path('voice/', views.create_text_v),
    path('button_click/', views.button_click_view, name='button_click'),
    
]