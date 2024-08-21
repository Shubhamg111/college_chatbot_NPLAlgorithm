from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .chatbot import NLPChatbot

def home(request):
    return render(request, 'home.html')


from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.shortcuts import render

@login_required
def chat_view(request):
    # Use a session key specific to the user to track page refresh
    session_key = f'page_loaded_{request.user.id}'
    
    if request.method == 'GET':
        if request.session.get(session_key, False):
            # If the session variable exists, clear the chat history for the current user
            ChatMessage.objects.filter(user=request.user).delete()
        else:
            # Set the session variable on the first load for this user
            request.session[session_key] = True

    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if user_message:
            chatbot = NLPChatbot()
            bot_response = chatbot.generate_response(user_message)

            # Save the conversation to the database
            ChatMessage.objects.create(
                user=request.user,
                message=user_message,
                response=bot_response
            )

    # Retrieve chat history for the current user
    chat_history = ChatMessage.objects.filter(user=request.user).order_by('timestamp')

    return render(request, 'chat.html', {'chat_history': chat_history})
    
from django.contrib.auth import login as auth_login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm, ProfileEditForm
from django.urls import reverse 

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    return render(request, 'profile.html',{'user': request.user})

@login_required
def profile_edit(request):
    instance=request.user
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=instance)
        return render(request, 'profile_edit.html', {'form': form})