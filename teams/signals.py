from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile, CustomUser
from .models import Team
from stats.models import Pit_stats, Match


@receiver(post_save, sender=CustomUser)
def create_team(sender, instance, created, **kwargs):
    if instance.is_team_admin and not Team.objects.filter(team_num = instance.team_num).exists():
        Team.objects.create(team_users = instance, team_num = instance.team_num)
    else:
        Team.objects.filter(team_num = instance.team_num).update(team_users = instance)
        