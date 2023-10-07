from django.shortcuts import render, redirect
from django.http import HttpResponse
from firebase_admin import db, auth

def addFriends(request):
   
    return render(request, 'friends/friend.html')

def submitFriends(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')  # Getting the email value
        print(f"{first_name} {last_name} {email}")

        user1 = auth.get_user_by_email(request.session['email'])
        uid = user1.uid

        root = db.reference()  # Push this new user ID to Firebase Realtime Database
        root.child("users").child(uid).child("friends").child(email).set({
            '-1': {
                'message': 'Start messaging'
            }
        })        
        target_email = "00@gmail.com"
        uid = search_email(target_email)
        if uid:
            print(f"The unique ID for email {target_email} is {uid}")
        else:
            print(f"No user found with email {target_email}")

        return redirect('login_success', username=user1.email)


def search_email(target_email):
    root = db.reference("users")
    data = root.get()
    for uid, user_data in data.items():
        if 'email' in user_data and user_data['email'] == target_email:
            return uid  # Return the unique ID (UID)
    return None  # Return None if email not found
