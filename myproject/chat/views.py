from django.shortcuts import render, redirect
from firebase_admin import db, auth
from gtts import gTTS
from pygame import mixer
import time
from django.http import HttpResponse


def chat_box_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        user = auth.get_user_by_email(request.session['email'])
        uid = user.uid
        print("UID from chatbox view" + uid)
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


def email_view(request, email):
    context = {'email': email}  # Initializing context with 'email'
    user = auth.get_user_by_email(request.session['email'])
    uid = user.uid
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            messages_ref = db.reference('users').child(uid).child('friends').child(email)
            new_message_ref = messages_ref.push()
            new_message_ref.set({'text': message})
        
    
    messages_ref1 = db.reference('users').child(uid).child('friends').child(email)
    messages1 = messages_ref1.get()
    #chat_messages1 = [{'content': message['text'], 'uid': message.get('uid', 'Unknown user')} for message in messages1.values()] if messages1 else []
    chat_messages1 = [{'content': message.get('text', 'Start Messaging'), 'uid': message.get('uid', 'Unknown user')} for message in messages1.values()] if messages1 else []
    context.update({'chat_messages': chat_messages1})
        
    return render(request, 'chat/email_page.html', context)


def button_click_view(request):
    print("Hello World")  
    user1 = auth.get_user_by_email(request.session['email'])
    uid = user1.uid
    print(uid)
    print(user1.email)
    return redirect('login_success', username=user1.email)


def create_text_v(request): 
    # your text you want to convert to audio
    my_text = "Hello, I am your Text-to-Speech service."

    # convert text to speech
    language = 'en'  # English
    my_obj = gTTS(text=my_text, lang=language, slow=False)

    # save the converted audio to a file
    audio_file = "welcome.mp3"
    my_obj.save(audio_file)

    # initialize the mixer
    mixer.init()

    # load the file and play it
    mixer.music.load(audio_file)
    mixer.music.play()

    # wait for the audio to finish playing
    while mixer.music.get_busy():
        time.sleep(1)

    return HttpResponse("Audio has started playing.")
