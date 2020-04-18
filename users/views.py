import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as LOGIN
from django.contrib.auth.decorators import login_required
from django.http import request, JsonResponse
from feedback.forms import FeedbackForm
from feedback.models import Feedback
from users.forms import UserCreationForm, UserLoginForm, UserChangeForm
from users.models import CustomUser, Profile
from teams.models import Team
from django.conf import settings
from django.template import loader
from stats.models import Pit_stats
from django.views.generic.edit import CreateView
from stats.models import Pit_stats
from .models import CustomUser
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.http import HttpResponse  
import random, string
import phonetic_alphabet as alpha
from stats.models import Pit_stats, Game_stats, Match



@login_required
def index(request):
  if request.method == 'POST':
    form = FeedbackForm(request.POST)
    if form.is_valid():
      form.save()
      first_name = form.cleaned_data['first_name'] 
      Feedback.objects.filter(first_name = first_name).update(team_num = request.user.team_num)
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
      user_obj = form.save()       
      username = form.cleaned_data['username']
      is_team_admin = form.cleaned_data['is_team_admin']
      team_num = form.cleaned_data['team_num']
      email = form.cleaned_data['email']          
      
      user = CustomUser.objects.filter(username = username)
      user.is_active = False
      current_site = get_current_site(request)
      email_subject = 'Activate Your Account'
      message = render_to_string('users/email.html', {
          'user': user,
          'domain': current_site.domain,
          'uid': urlsafe_base64_encode(force_bytes(user_obj.pk)),
          'token': account_activation_token.make_token(user_obj),
      })

      email = EmailMessage(email_subject, message, to=['frcsassistant@gmail.com'])
      email.send()

      #user.first().email_verify()
      #send_mail_to = form.cleaned_data['email']
      if is_team_admin:
        user.update(is_team_admin = True)
      if not Team.objects.filter(team_num = team_num).exists():
        
        VID = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)))
        Team.objects.create(team_users = user_obj, team_num = team_num, team_code = VID)
      LOGIN(request, user_obj)
      return redirect('welcome-view')    
        #TEMPLATE CODE
    else:
        #Registration error check
        messages.warning(request, f'Registration invalid. Username/Email already exists')     
  return render(request, 'users/register.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/welcome.html')
    else:
        return HttpResponse('Activation link is invalid!')
        
def gettingStarted(request):
  return render(request, 'users/getting-started.html')


def guest(request):
  return render(request, 'users/guest.html')

def media(request):
  return render(request, 'users/media.html')

@login_required
def welcome(request):
  return render(request, 'users/welcome.html')

@login_required
def forgot(request):
  return render(request, 'users/forgot-pass.html')

def verify(request):
  return render(request, 'users/verify.html')

@login_required
def ProfileSettings(request):
  if request.method == 'POST':
    form = UserChangeForm(request.POST, instance=request.user)
    if form.is_valid:
      form.save()
      return redirect('profile-view')
  return render(request, 'users/profile-settings.html')

def getAuthLevel():
  if CustomUser.is_team_admin:
    return "Team Mentor"
  else: 
    return "Team Member"

@login_required
def profile(request):      


  context = {
      'user_admins': CustomUser.objects.filter(team_num = request.user.team_num, is_team_admin = True),
      'users': CustomUser.objects.filter(team_num = request.user.team_num, is_team_admin = False),
      'auth_level': getAuthLevel(),
      'code': Team.objects.get(team_num=request.user.team_num).team_code,
      'phonetic': alpha.read(Team.objects.get(team_num=request.user.team_num).team_code)
  }
  return render(request, 'users/profile.html', context)


          #send_mail_to = form.cleaned_data['email']
class JSONResponseMixin:
  """
  A mixin that can be used to render a JSON response.
  """
  def render_to_json_response(self, context, **response_kwargs):
      """
      Returns a JSON response, transforming 'context' to make the payload.
      """
      return JsonResponse(
          self.get_data(context),
          **response_kwargs
      )

  def get_data(self, context):
      """
      Returns an object that will be serialized as JSON by json.dumps().
      """
      # Note: This is *EXTREMELY* naive; in reality, you'll need
      # to do much more complex handling to ensure that arbitrary
      # objects -- such as Django model instances or querysets
      # -- can be serialized as JSON.
      return context
    
@login_required
def teamManagement(request):
  
  game_list = Match.objects.filter(team_num=request.user.team_num)
  context = {
              'users': CustomUser.objects.filter(team_num = request.user.team_num, is_team_admin = False), 
              'game': game_list,
              'image': Profile.image #!NOT DISPLAYING IMAGE - JUST SHOWING PLACEHOLDER
  }
        
  return render(request, 'users/team-manager.html', context)

def accountDeleted(request):
  instance = CustomUser.objects.get(username = request.user)
  instance.delete()
  return render(request, 'users/account-delete.html')

def managerDelete(request):
    instance = Team.objects.get(team_num = request.user.team_num)
    instance.delete()
    return render(request, 'users/manager-delete.html')
  
  