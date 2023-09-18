# chat/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('friends/', views.addFriends, name='add_contacts'),
    path('submit_friend/', views.submitFriends, name='submit_friend'),
]