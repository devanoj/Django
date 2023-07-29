# chat/views.py

from django.shortcuts import render

def chat_box_view(request):
    # Your chat box view logic goes here
    return render(request, 'chat/chat_box.html')