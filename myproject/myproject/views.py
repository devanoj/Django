from django.http import HttpResponse, JsonResponse
import requests
import firebase_admin
from firebase_admin import credentials, db

PATH = r'C:\Users\devan\$Firebase Key\django-chat-app-4235d-firebase-adminsdk-q2yo9-af4cd7cce7.json'
cred = credentials.Certificate(PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://django-chat-app-4235d-default-rtdb.firebaseio.com/'
})

def hello_world(request):
    return HttpResponse("Hello, World!")

def get_firebase_data(request):
    ref1 = db.reference('pyTest/')
    tests_ref = ref1.child('childTest')
    tests_ref.set({
    'Test1': {
        'Test':'1',
        'Attempt':'1'
    },
    'Test2': {
        'Test':'2',
        'Attempt':'2'
    }
    
})


def api_test_view(request):
    api_url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            users_data = response.json()
            data_to_display = []
            for user in users_data:
                data_to_display.append({"name": user['name'], "email": user['email']})
            return JsonResponse(data_to_display, safe=False)
        else:
            return JsonResponse({"error": f"Request returned status code {response.status_code}"}, status=500)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
