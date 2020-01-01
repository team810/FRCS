from django.shortcuts import render, redirect
from users.forms import UserCreationForm, UserLoginForm
from django.contrib.auth import login as LOGIN
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import request
from users.models import CustomUser
from feedback.forms import FeedbackForm

#from .forms import CustomUserCreationForm
#from .models import UserProfile
#from .backends import CustomUserAuth as auth
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            team_num = form.cleaned_data.get('team_num')
            message = form.cleaned_data.get('message')
            return redirect('home-view')
    else:
        form = FeedbackForm()
    return render(request, 'users/index.html', {'form': form})

def login(request):
    form = UserLoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if request.method == 'POST':
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            LOGIN(request, user_obj)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home-view')
        else:
            messages.warning(request, f'Invalid Credentials')
    
    return render(request, 'users/login.html', {"form": form})

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            is_team_admin = form.cleaned_data['is_team_admin']
            username = form.cleaned_data['username']
            user_obj = form.save()
            if is_team_admin:
                CustomUser.objects.filter(username = username).update(is_team_admin = True)
            LOGIN(request, user_obj)
            return redirect('home-view')
        else:
            #Registration error check
            messages.warning(request, f'Registration invalid. Username/Email already exists')
    return render(request, 'users/register.html', {'form': form})

def scout(request):
    return render(request, 'users/scout.html')

def scouthub(request):
    return render(request, 'users/scouthub.html')

def gettingStarted(request):
    return render(request, 'users/gettingStarted.html')


def admin(request):
    return render(request, 'users/admin.html')

@login_required
def welcome(request):
    return render(request, 'users/welcome.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

