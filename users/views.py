import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as LOGIN
from django.contrib.auth.decorators import login_required
from django.http import request, JsonResponse
from django.core.mail import send_mail
from feedback.forms import FeedbackForm
from feedback.models import Feedback
from users.forms import UserCreationForm, UserLoginForm, UserChangeForm
from users.models import CustomUser
from teams.models import Team
from django.conf import settings
from django.template import loader
import smtplib
from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
from stats.models import Pit_stats
from django.views.generic.edit import CreateView
from stats.models import Pit_stats

# Create your views here.

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
      #user.first().email_verify()
      #send_mail_to = form.cleaned_data['email']
      if is_team_admin:
        user.update(is_team_admin = True)
      if not Team.objects.filter(team_num = team_num).exists():
        Team.objects.create(team_users = user_obj, team_num = team_num)
      LOGIN(request, user_obj)
      return redirect('welcome-view')    
        #TEMPLATE CODE
    else:
        #Registration error check
        messages.warning(request, f'Registration invalid. Username/Email already exists')       
  return render(request, 'users/register.html', {'form': form})

def gettingStarted(request):
  return render(request, 'users/getting-started.html')

def admin(request):
  return render(request, 'users/admin.html')

def guest(request):
  return render(request, 'users/guest.html')

def media(request):
  return render(request, 'users/media.html')

@login_required
def welcome(request):
  html_message = loader.render_to_string('users/email.html')
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


@login_required
def profile(request):
  context = {
      'user_admins': CustomUser.objects.filter(team_num = request.user.team_num, is_team_admin = True),
      'users': CustomUser.objects.filter(team_num = request.user.team_num, is_team_admin = False),
  }
  return render(request, 'users/profile.html', context)

#TEMP CODE
'''template = os.path.abspath('users/email_template.html')
        msg = MIMEMultipart('alternative')
        htmly = MIMEText(template, 'html')
        msg.attach(htmly)
        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
          smtp.ehlo()
          smtp.starttls()
          smtp.ehlo()
          smtp.login("frcsassistant@gmail.com", "zikpniouyggoqfmk")
          smtp.sendmail('frcsassistant@gmail.com','frcsassistant@gmail.com', msg.as_string())''' 
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