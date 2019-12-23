from django.shortcuts import render, redirect


from .forms import CustomUserCreationForm
from .models import User, MyUserManager
# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def scout(request):
    context = {
        'count': 20
    }
    return render(request, 'users/scout.html', count)

def scouthub(request):
    return render(request, 'users/scouthub.html')