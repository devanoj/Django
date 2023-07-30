from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from django.shortcuts import render, redirect



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # Use 'email' instead of 'username' for Firebase
        password = request.POST.get('password')

        try:
            # Authenticate the user with Firebase
            user = auth.get_user_by_email(email)
            print('Successfully fetched user data: {0}'.format(user.uid))
            
            
            # If there is no exception raised, the user exists and authentication succeeded
            username = email
            
            return redirect('login_success', username=username)
        except auth.AuthError as e:
            # Handle authentication failure
            print('Authentication error:', str(e))

    # Handle failed login (e.g., display an error message)
    return render(request, 'loginapp/login.html', {'error_message': 'Invalid credentials'})

def success_view(request, username):
    return render(request, 'loginapp/success.html', {'username': username})

def settings_view(request):
    # Your settings view logic goes here
    return render(request, 'loginapp/settings.html')

def signup_view(request):
    error_message = None
    
    if request.method == 'POST':
        email = request.POST.get('username')  # Use 'email' instead of 'username' for Firebase
        password = request.POST.get('password')

        try:
            # Create the user in Firebase
            user = auth.create_user(email=email, password=password)
            return redirect('login')
            # User created successfully
        except Exception as e:
            # Handle any other exception that might occur during the signup process
            error_message = 'An error occurred during signup. Please try again.'

        
    return render(request, 'loginapp/signup.html', {'error_message': error_message})




