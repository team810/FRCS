import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as LOGIN
from django.contrib.auth.decorators import login_required
from django.http import request, JsonResponse
from feedback.forms import FeedbackForm
from feedback.models import Feedback
from users.forms import (
    UserCreationForm,
    UserLoginForm,
    UserChangeForm,
    UserEditForm,
    ProfileEditForm,
    NameEditForm,
)
from users.models import CustomUser, Profile
from teams.models import Team
from django.conf import settings
from django.template import loader
from stats.models import Pit_stats, Game_stats, Match
from django.views.generic.edit import CreateView
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
from stats.forms import pit_scout_form, game_scout_form
from django.shortcuts import get_object_or_404



def index(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data["first_name"]
            Feedback.objects.filter(first_name=first_name).update(
                team_num=request.user.team_num
            )
            return redirect("home-view")
    else:
        form = FeedbackForm()
    return render(request, "users/index.html", {"form": form})


def login(request):
    form = UserLoginForm(request.POST or None)
    next_url = request.GET.get("next")
    if request.method == "POST":
        if form.is_valid():
            user_obj = form.cleaned_data.get("user_obj")
            LOGIN(request, user_obj)

            if next_url:
                return redirect(next_url)
            else:
                return redirect("home-view")

        else:
            messages.warning(request, f"Invalid Credentials")

    return render(request, "users/login.html", {"form": form})


def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user_obj = form.save()        
            username = form.cleaned_data["username"]
            is_team_admin = form.cleaned_data["is_team_admin"]
            team_num = form.cleaned_data["team_num"]
            email = form.cleaned_data["email"]
            user = CustomUser.objects.filter(username=username)
            user.is_active = False
            current_site = get_current_site(request)
            email_subject = "Activate Your Account"
            message = render_to_string(
                "users/email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user_obj.pk)),
                    "token": account_activation_token.make_token(user_obj),
                },
            )

            email = EmailMessage(
                email_subject, message, to=["frcsassistant@gmail.com"]
            )  #!change to form.cleaned_data['email'] in prod
            email.send()

            # user.first().email_verify()
            if is_team_admin:
                user.update(is_team_admin=True)
            if not Team.objects.filter(team_num=team_num).exists():

                VID = str(
                    "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
                )
                Team.objects.create(
                    team_users=user_obj, team_num=team_num, team_code=VID
                )
            LOGIN(request, user_obj)
            return redirect("welcome-view")
            # TEMPLATE CODE
        else:
            # Registration error check
            messages.warning(
                request, f"Registration invalid. Username/Email already exists"
            )
    context = {
        'form': form,
    }
    return render(request, "users/register.html", context)


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "users/welcome.html")
    else:
        return HttpResponse("Activation link is invalid!")


def gettingStarted(request):
    return render(request, "users/getting-started.html")


def guest(request):
    return render(request, "users/guest.html")


def media(request):
    return render(request, "users/media.html")


@login_required
def welcome(request):
    return render(request, "users/welcome.html")


def verify(request):
    return render(request, "users/verify.html")


def getAuthLevel():
    if CustomUser.is_team_admin:
        return "Team Mentor"
    else:
        return "Team Member"


@login_required
def ProfileSettings(request):
    form = NameEditForm(request.POST, instance=request.user.profile)
    context = {
        "auth_level": getAuthLevel(),
        "form": form,
        "picture": request.user.profile.image
    }
    if request.method == "POST":
        form = NameEditForm(request.POST, instance=request.user.profile)
        if form.is_valid:
            form.save()
            return redirect("profile-view")
    return render(request, "users/profile-settings.html", context)


@login_required
def profile(request):

    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
        "phonetic": alpha.read(Team.objects.get(team_num=request.user.team_num).team_code),
        "picture": request.user.profile.image,
        'stat': Match.objects.filter(user=request.user),
        'game_num': Match.objects.filter(user=request.user).count(),
        'team_game_num': Match.objects.filter(team_num=request.user.team_num).count(),
        'global_game_num': Match.objects.filter(scouted_team_num=request.user.team_num).count(),
        'pit_num': Pit_stats.objects.filter(user=request.user).count(),
        'team_pit_num': Pit_stats.objects.filter(scouted_team_num=request.user.team_num).count(),
        'global_pit_num': Pit_stats.objects.filter(team_num=request.user.team_num).count()
    }
    return render(request, "users/profile.html", context)

    # send_mail_to = form.cleaned_data['email']


class JSONResponseMixin:
    """
  A mixin that can be used to render a JSON response.
  """

    def render_to_json_response(self, context, **response_kwargs):
        """
      Returns a JSON response, transforming 'context' to make the payload.
      """
        return JsonResponse(self.get_data(context), **response_kwargs)

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
    try:
        pit_list = Pit_stats.objects.get(team_num=request.user.team_num)
    except:
        pit_list = None
    team_num = Team.objects.filter(team_num=request.user.team_num)
    if team_num and pit_list:
        context = {
            "users": CustomUser.objects.filter(
                team_num=request.user.team_num, is_team_admin=False
            ),
            "game": game_list,
            "pit": pit_list,
            "image": Profile.image,  
            "team_num": team_num,
        }
    else:
        context = {
            "users": CustomUser.objects.filter(
                team_num=request.user.team_num, is_team_admin=False
            ),
            "game": game_list,
            "image": Profile.image, 
            'pit': pit_list
        }
    
    return render(
        request, "users/team-manager.html", context
    )  #!NEED TO RENDER MODEL IF THERE IS NOT PIT DATA FOR RESPECTIVE TEAM
    #!REMOVE CONTEXT FROM RENDER IN **IF ELSE STATEMENT** / **TRY EXCEPT**



def changelog(request):
    return render(request, "users/changelog.html")


def pitUpdate(request, team_num):
    instance = Pit_stats.objects.get(team_num=request.user.team_num)
    form = pit_scout_form(request.POST or None, instance=instance)
    context = {"instance": instance, "form": form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request, "users/team-manager.html", context)

    return render(request, "users/pit-update.html", context)


def imageUpload(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES,  instance=request.user.profile)
    else:
        form = ProfileEditForm(instance=request.user.profile)

        if form.is_valid():
            form.save()
    context = {
        "form": form,
        'image': request.user.profile.image,
    }
    return render(request, "users/image-upload.html", context)

def accountEdit(request):
    form = UserEditForm(request.POST, instance=request.user)
    context = {
        "auth_level": getAuthLevel(),
        "form": form,
        "picture": request.user.profile.image,
    }
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect("profile-view")
    return render(request, 'users/account-edit.html', context)

@login_required
def profileGameEntries(request):
    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
        "phonetic": alpha.read(Team.objects.get(team_num=request.user.team_num).team_code),
        "picture": request.user.profile.image,
        'stat': Match.objects.filter(user=request.user),
        'game_num': Match.objects.filter(user=request.user).count(),
        'team_game_num': Match.objects.filter(team_num=request.user.team_num).count(),
        'global_game_num': Match.objects.filter(scouted_team_num=request.user.team_num).count(),
        'pit_num': Pit_stats.objects.filter(user=request.user).count(),
        'team_pit_num': Pit_stats.objects.filter(scouted_team_num=request.user.team_num).count(),
                'global_pit_num': Pit_stats.objects.filter(team_num=request.user.team_num).count()


    }
    return render(request, 'users/profile-game-entries.html', context)


@login_required
def profilePitEntries(request):

    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
        "phonetic": alpha.read(Team.objects.get(team_num=request.user.team_num).team_code),
        "picture": request.user.profile.image,
        'stat': Pit_stats.objects.filter(user=request.user), #!NEEDS TO BE CHANGED TO PIT STATS FOR PERSONAL SCOPE
        'game_num': Match.objects.filter(user=request.user).count(),
        'team_game_num': Match.objects.filter(team_num=request.user.team_num).count(),
        'global_game_num': Match.objects.filter(scouted_team_num=request.user.team_num).count(),
        'pit_num': Pit_stats.objects.filter(user=request.user).count(),
        'team_pit_num': Pit_stats.objects.filter(scouted_team_num=request.user.team_num).count(),
        'global_pit_num': Pit_stats.objects.filter(team_num=request.user.team_num).count()
    }
    return render(request, 'users/profile-pit-entries.html', context)

@login_required
def teamGameEntries(request):
    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
        "phonetic": alpha.read(Team.objects.get(team_num=request.user.team_num).team_code),
        "picture": request.user.profile.image,
        'stat': Match.objects.filter(team_num=request.user.team_num),
        'game_num': Match.objects.filter(user=request.user).count(),
        'team_game_num': Match.objects.filter(team_num=request.user.team_num).count(),
        'global_game_num': Match.objects.filter(scouted_team_num=request.user.team_num).count(),
        'pit_num': Pit_stats.objects.filter(user=request.user).count(),
        'team_pit_num': Pit_stats.objects.filter(scouted_team_num=request.user.team_num).count(),
        'global_pit_num': Pit_stats.objects.filter(team_num=request.user.team_num).count()
    }
    
    return render(request, 'users/team-game-entries.html', context)

@login_required
def teamPitEntries(request):
    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
        "phonetic": alpha.read(Team.objects.get(team_num=request.user.team_num).team_code),
        "picture": request.user.profile.image,
        'stat': Pit_stats.objects.filter(scouted_team_num=request.user.team_num), 
        'game_num': Match.objects.filter(user=request.user).count(),
        'team_game_num': Match.objects.filter(team_num=request.user.team_num).count(),
        'global_game_num': Match.objects.filter(scouted_team_num=request.user.team_num).count(),
        'pit_num': Pit_stats.objects.filter(user=request.user).count(),
        'team_pit_num': Pit_stats.objects.filter(scouted_team_num=request.user.team_num).count(),
        'global_pit_num': Pit_stats.objects.filter(team_num=request.user.team_num).count()

    }
    return render(request, 'users/team-pit-entries.html', context)

@login_required
def globalGameEntries(request):
    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
        "phonetic": alpha.read(Team.objects.get(team_num=request.user.team_num).team_code),
        "picture": request.user.profile.image,
        'stat': Match.objects.filter(scouted_team_num=request.user.team_num),
        'game_num': Match.objects.filter(user=request.user).count(),
        'team_game_num': Match.objects.filter(team_num=request.user.team_num).count(),
        'global_game_num': Match.objects.filter(scouted_team_num=request.user.team_num).count(),
        'pit_num': Pit_stats.objects.filter(user=request.user).count(),
        'team_pit_num': Pit_stats.objects.filter(scouted_team_num=request.user.team_num).count(),
        'global_pit_num': Pit_stats.objects.filter(team_num=request.user.team_num).count()
    }
    return render(request, 'users/global-game-entries.html', context)

@login_required
def globalPitEntries(request):
    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
        "phonetic": alpha.read(Team.objects.get(team_num=request.user.team_num).team_code),
        "picture": request.user.profile.image,
        'stat': Pit_stats.objects.filter(team_num=request.user.team_num), 
        'game_num': Match.objects.filter(user=request.user).count(),
        'team_game_num': Match.objects.filter(team_num=request.user.team_num).count(),
        'global_game_num': Match.objects.filter(scouted_team_num=request.user.team_num).count(),
        'pit_num': Pit_stats.objects.filter(user=request.user).count(),
        'team_pit_num': Pit_stats.objects.filter(scouted_team_num=request.user.team_num).count(),
        'global_pit_num': Pit_stats.objects.filter(team_num=request.user.team_num).count()
    }
    return render(request, 'users/global-pit-entries.html', context)