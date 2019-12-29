from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feedback.models import Feedback
# Create your views here.

@login_required
def feedbackView(request):
    if request.user.is_admin:
        context = {
            'feedback': Feedback.objects.all()
        }
        return render(request, 'feedback/feedback.html', context)
    else:
        return render(request, 'users/index.html')
