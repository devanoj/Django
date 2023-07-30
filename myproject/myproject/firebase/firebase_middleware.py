from django.utils.deprecation import MiddlewareMixin
from firebase_admin import credentials, initialize_app, db, get_app
import os

class FirebaseMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        # Set up Firebase DB.
        cred_path = r'C:\Users\devan\$Firebase Key\django-chat-app-4235d-firebase-adminsdk-q2yo9-af4cd7cce7.json'
        databaseURL = 'https://django-chat-app-4235d-default-rtdb.firebaseio.com/'
        try:
            app = get_app()  # try to get the default app
        except ValueError as e:
            # Initialize the firebase app if it doesn't exist
            cred = credentials.Certificate(cred_path)
            initialize_app(cred, {
                'databaseURL': databaseURL
            })
