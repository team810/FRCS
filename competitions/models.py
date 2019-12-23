from django.db import models

# Create your models here.
class Competitions(Models.model):
    id = models.ForeignKey
    event_code = models.CharField(max_length = 100)
    event_name =  models.CharField(max_length = 100)
    
    def __str__(self):
        return self.id