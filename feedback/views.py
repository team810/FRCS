from django.shortcuts import render

# Create your views here.

def feedbackView(request):
    return render(request, 'feedback/feedback.html')
