from django.shortcuts import render

def addFriends(request):
    return render(request, 'friends/friend.html')

# Create your views here.
