from django.shortcuts import render

# Create your views here.

def apiView(request):
    return render(request, 'api/api.html')