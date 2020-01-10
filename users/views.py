from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as LOGIN
from django.contrib.auth.decorators import login_required
from django.http import request
#from django.core.mail import send_mail
from feedback.forms import FeedbackForm
from users.forms import UserCreationForm, UserLoginForm, UserChangeForm
from users.models import CustomUser
from teams.models import Team
#from .forms import CustomUserCreationForm
#from .models import UserProfile
#from .backends import CustomUserAuth as auth
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
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
            username = form.cleaned_data['username']
            is_team_admin = form.cleaned_data['is_team_admin']
            #send_mail_to = form.cleaned_data['email']
            user_obj = form.save()
            if is_team_admin:
                CustomUser.objects.filter(username = username).update(is_team_admin = True)
            #send_mail('Test Mail',
            #'Test Mail',
            #'FRCScoutingNoReplay@gmail.com',
            #[send_mail_to],
            #fail_silently=False)
            LOGIN(request, user_obj)
            return redirect('welcome-view')
        else:
            #Registration error check
            messages.warning(request, f'Registration invalid. Username/Email already exists')
    return render(request, 'users/register.html', {'form': form})

def scout(request):
    return render(request, 'users/scout.html')

def Pitscout(request):
    return render(request, 'users/PitScout.html')

def scouthub(request):
    return render(request, 'users/scouthub.html', {'team_count': Team.objects.all().count()})

def gettingStarted(request):
    return render(request, 'users/gettingStarted.html')


def admin(request):
    return render(request, 'users/admin.html')

def guest(request):
    return render(request, 'users/guest.html')

def media(request):
    return render(request, 'users/media.html')

def pitdata(request):
    return render(request, 'users/pitData.html')

def gamedata(request):
    return render(request, 'users/gameData.html')

@login_required
def welcome(request):
    return render(request, 'users/welcome.html')

@login_required
def forgot(request):
    return render(request, 'users/forgotPass.html')

@login_required
def feed(request):
    return render(request, 'users/feed.html')

@login_required
def ProfileSettings(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('profile-view')
    return render(request, 'users/profile-settings.html')


@login_required
def profile(request):
    context = {
        'user_admins': CustomUser.objects.filter(team_num = request.user.team_num, is_team_admin = True),
        'users': CustomUser.objects.filter(team_num = request.user.team_num, is_team_admin = False),
    }
    return render(request, 'users/profile.html', context)
