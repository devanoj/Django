# chat/views.py
import firebase_admin
from firebase_admin import credentials, db
from django.shortcuts import render

def chat_box_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message.strip():
            # Save the chat message to Firebase Realtime Database
            messages_ref = db.reference('chat_messages')
            new_message_ref = messages_ref.push()
            new_message_ref.set({
                'content': message
            })

    # Fetch chat messages from Firebase
    messages_ref = db.reference('chat_messages')
    messages = messages_ref.get()

    # Convert Firebase response to a list of messages
    chat_messages = [message['content'] for message in messages.values()] if messages else []

    context = {
        'chat_messages': chat_messages
    }

    return render(request, 'chat/chat_box.html', context)