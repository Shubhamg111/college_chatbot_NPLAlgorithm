from django.urls import path
from .views import *




urlpatterns = [
    path('',home,name='home'),
    path('chat/', chat_view, name='chat'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/', profile, name='profile'),
    path('logout/',logoutuser, name='logout')
]
