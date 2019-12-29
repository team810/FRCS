from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    first_name = models.CharField(max_length=254, verbose_name="First Name")
    team_num = models.IntegerField(verbose_name="Team Number")
    message = models.TextField(verbose_name="Message", max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name

    
