from django.shortcuts import render
from firebase_admin import db, auth

def chat_box_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        user = auth.get_user_by_email(request.session['email'])
        uid = user.uid
        if message.strip() and uid:
            # Save the chat message to Firebase Realtime Database
            messages_ref = db.reference('chat_messages')
            new_message_ref = messages_ref.push()
            new_message_ref.set({
                'content': message,
                'uid': uid  # include the uid when you push a new message
            })

    # Fetch chat messages from Firebase
    messages_ref = db.reference('chat_messages')
    messages = messages_ref.get()

    # Convert Firebase response to a list of messages
    chat_messages = [{'content': message['content'], 'uid': message.get('uid', 'Unknown user')} for message in messages.values()] if messages else []

    context = {
        'chat_messages': chat_messages
    }

    return render(request, 'chat/chat_box.html', context)
