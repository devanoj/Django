from django.http import HttpResponse
from django.http import JsonResponse
import requests

def hello_world(request):
    return HttpResponse("Hello, World!")

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
