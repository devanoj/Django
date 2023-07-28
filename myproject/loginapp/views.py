from django.shortcuts import render

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Implement your login logic here, such as authentication and redirecting to the dashboard page on success.
        # For demonstration purposes, we will simply return a success message for now.
     
    
    return render(request, 'loginapp/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    
    return render(request, 'loginapp/signup.html')

