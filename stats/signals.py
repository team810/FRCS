from django.db.models.signals import post_save
from django.dispatch import receiver
from teams.models import Team
from .models import Pit_stats

@receiver(post_save, sender=Team)
def create_stats(sender, instance, created, **kwargs):
    Pit_stats.objects.create(team = instance)