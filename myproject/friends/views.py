from django.shortcuts import render, redirect
from django.http import HttpResponse
from firebase_admin import db, auth

def addFriends(request):
    return render(request, 'friends/friend.html')

def submitFriends(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')

        # Your code for adding friends here
        # For now, we're printing the submitted data
        print(f"{first_name} {last_name} {email}")

        user1 = auth.get_user_by_email(request.session['email'])
        
        return redirect('login_success', username=user1.email)