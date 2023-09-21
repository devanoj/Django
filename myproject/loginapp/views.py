from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth, db
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

            # Store the user's email in the session
            request.session['email'] = email

            


            return redirect('login_success', username=username)
        except auth.AuthError as e:
            # Handle authentication failure
            print('Authentication error:', str(e))

    # Handle failed login (e.g., display an error message)
    return render(request, 'loginapp/login.html', {'error_message': 'Invalid credentials'})


def success_view(request, username):
    user1 = auth.get_user_by_email(request.session['email'])
    uid = user1.uid
    messages_ref = db.reference('users').child(uid).child("friends")
    messages = messages_ref.get() or {}

    # Extracting only the values (emails) from the messages
    emails = list(messages.values())

    # Define a context dictionary to hold your variables
    context = {
        'username': username,
        'emails': emails  # Passing only the email values to the context
    }

    # Pass the context dictionary to the render function
    return render(request, 'loginapp/success.html', context)

def settings_view(request):
    # Your settings view logic goes here
    return render(request, 'loginapp/settings.html')

def friends_view(request):
    return render(request, )

def signup_view(request):
    error_message = None
    
    if request.method == 'POST':
        email = request.POST.get('username')  # Use 'email' instead of 'username' for Firebase
        password = request.POST.get('password')

        try:
            # Create the user in Firebase
            user = auth.create_user(email=email, password=password)
            print(user.uid)

           
            user_id = user.uid  # Get user ID (uid) from Firebase
            print(f"Successfully created new user: {user_id}")

            
            root = db.reference()  # Push this new user ID to Firebase Realtime Database
            root.child('users').child(user_id).set({
                'email': email,
                'password': password,  # Storing passwords like this is insecure. This is just for demonstration.
                'friends': ["test1", "test2"]
            })

            return redirect('login')
        
        except Exception as e:
            error_message = 'An error occurred during signup. Please try again.'

        
    return render(request, 'loginapp/signup.html', {'error_message': error_message})




