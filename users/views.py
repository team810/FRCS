from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as LOGIN
from django.contrib.auth.decorators import login_required
from django.http import request
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



#from .forms import CustomUserCreationForm
#from .models import UserProfile
#from .backends import CustomUserAuth as auth
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
            
            template = """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900&display=swap" rel="stylesheet">
  <style type="text/css" rel="stylesheet" media="all">
  
    
    body {
      width: 100% !important;
      height: 100%;
      margin: 0;
      line-height: 1.4;
      background-color: #F5F7F9;
      color: #839197;
      -webkit-text-size-adjust: none;
      font-family: 'poppins', 'sans-serif'
    }
    a {
      color: #414EF9;
    }

    /* Layout ------------------------------ */
    .email-wrapper {
      width: 100%;
      margin: 0;
      padding: 0;
      background-color: #F5F7F9;
    }
    .email-content {
      width: 100%;
      margin: 0;
      padding: 0;
    }

    /* Masthead ----------------------- */
    .email-masthead {
      padding: 25px 0;
      text-align: center;
    }
    .email-masthead_logo {
      max-width: 400px;
      border: 0;
    }
    .email-masthead_name {
      font-size: 16px;
      font-weight: bold;
      color: #839197;
      text-decoration: none;
      text-shadow: 0 1px 0 white;
    }

    /* Body ------------------------------ */
    .email-body {
      width: 100%;
      margin: 0;
      padding: 0;
      border-top: 1px solid #E7EAEC;
      border-bottom: 1px solid #E7EAEC;
      background-color: #FFFFFF;
    }
    .email-body_inner {
      width: 570px;
      margin: 0 auto;
      padding: 0;
    }
    .email-footer {
      width: 570px;
      margin: 0 auto;
      padding: 0;
      text-align: center;
    }
    .email-footer p {
      color: #839197;
    }
    .body-action {
      width: 100%;
      margin: 30px auto;
      padding: 0;
      text-align: center;
    }
    .body-sub {
      margin-top: 25px;
      padding-top: 25px;
      border-top: 1px solid #E7EAEC;
    }
    .content-cell {
      padding: 35px;
    }
    .align-right {
      text-align: right;
    }

    /* Type ------------------------------ */
    h1 {
      margin-top: 0;
      color: #292E31;
      font-size: 19px;
      font-weight: bold;
      text-align: left;
    }
    h2 {
      margin-top: 0;
      color: #292E31;
      font-size: 16px;
      font-weight: bold;
      text-align: left;
    }
    h3 {
      margin-top: 0;
      color: #292E31;
      font-size: 14px;
      font-weight: bold;
      text-align: left;
    }
    p {
      margin-top: 0;
      color: #839197;
      font-size: 16px;
      line-height: 1.5em;
      text-align: left;
    }
    p.sub {
      font-size: 12px;
    }
    p.center {
      text-align: center;
    }

    /* Buttons ------------------------------ */
    .button {
      display: inline-block;
      width: 200px;
      background-color: lightblue;
      border-radius: 5px;
      color: #ffffff;
      font-size: 15px;
      line-height: 45px;
      text-align: center;
      font-weight: bold;
      text-decoration: none;
      -webkit-text-size-adjust: none;
      mso-hide: all;
      border-color: transparent;
    }

    /*Media Queries ------------------------------ */
    @media only screen and (max-width: 600px) {
      .email-body_inner,
      .email-footer {
        width: 100% !important;
      }
    }
    @media only screen and (max-width: 500px) {
      .button {
        width: 100% !important;
      }
    }

    #title{
        font-size: 40px;
    }
  </style>
</head>
<body>

  <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0">
    <tr>
      <td align="center">
        <table class="email-content" width="100%" cellpadding="0" cellspacing="0">
          <!-- Logo -->
          <tr>
            <td class="email-masthead">
            </td>
          </tr>
          <!-- Email Body -->
          <tr>
            <td class="email-body" width="100%">
              <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0">
                <!-- Body content -->
                <tr>
                  <td class="content-cell">
                  <h1 id="title"><strong>FRCS</strong></h1>
                    <h1>Verify your email address</h1>
                    <p>Thanks for signing up for FRCS! We're excited to have you as a user.</p>
                    <p>Click the button below to verify your account</p>
                    <!-- Action -->
                    <table class="body-action" align="center" width="100%" cellpadding="0" cellspacing="0">
                      <tr>
                        <td align="center">
                          <div>
                            <form action="frcs.online/verify">
                              <button class="button" type="submit">Click me</button>
                            </form>
                          </div>
                        </td>
                      </tr>
                    </table>
                    <p>Contact support</p><a>frcsassistant@gmail.com</a>
                    <p>Thanks,<br>The FRCS Team</p>
                    <!-- Sub copy -->
                    <table class="body-sub">
                      <tr>
                        <td>
                          <p class="sub">If you’re having trouble clicking the button, copy and paste the URL below into your web browser.
                          </p>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
             
      </td>
    </tr>
  </table>
</body>
</html>"""
            username = form.cleaned_data['username']
            is_team_admin = form.cleaned_data['is_team_admin']
            team_num = form.cleaned_data['team_num']
            email = form.cleaned_data['email']
            N = 7
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N)) 
  
            VID = str(res)
            print(VID)

            msg = MIMEMultipart('alternative')
            htmly = MIMEText(template, 'html')
            msg.attach(htmly)
            
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login("frcsassistant@gmail.com", "zikpniouyggoqfmk")
                smtp.sendmail('frcsassistant@gmail.com','frcsassistant@gmail.com', msg.as_string())          

            #send_mail_to = form.cleaned_data['email']
            user_obj = form.save()
            if is_team_admin:
                CustomUser.objects.filter(username = username).update(is_team_admin = True)
                if not Team.objects.filter(team_num = team_num).exists():
                    p = Team.objects.create(team_users = user_obj, team_num = team_num)

                #else:     
            LOGIN(request, user_obj)
            return redirect('welcome-view')
        else:
            #Registration error check
            messages.warning(request, f'Registration invalid. Username/Email already exists')
    return render(request, 'users/register.html', {'form': form})
@login_required
def scout(request):
    return render(request, 'users/scout.html')
@login_required
def Pitscout(request):
    return render(request, 'users/PitScout.html')

def scouthub(request):
    return render(request, 'users/ScoutHub.html', {'team_count': Team.objects.all().count()})

def gettingStarted(request):
    return render(request, 'users/GettingStarted.html')


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
    html_message = loader.render_to_string('users/email.html')
    return render(request, 'users/welcome.html')

@login_required
def forgot(request):
    return render(request, 'users/forgotPass.html')

@login_required
def feed(request):
    return render(request, 'users/feed.html')

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

