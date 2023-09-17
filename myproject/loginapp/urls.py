# loginapp/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('success/<str:username>/', views.success_view, name='login_success'),  
    path('settings/', views.settings_view, name='settings'),
    path('chat/', include('chat.urls')),
    path('addFriends/', include('friends.urls')),
]
