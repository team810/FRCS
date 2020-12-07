from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Game_stats
from teams.models import Team
from stats.models import Match, Competition

@receiver(post_save, sender=Team)
def create_game_stats(sender, instance, created, **kwargs):
    if created:
        Game_stats.objects.create(team = instance)


@receiver(post_save, sender=Match)
def create_comp(sender, instance, created, **kwargs):
    if created:
        comp = Competition.objects.latest('competition')
        Competition.objects.create(competition = comp, match_num = instance)
        try:
            Competition.objects.all()[Competition.objects.count()-2].delete()
        except:
            pass

#!Aaquib dont bully me - This is incredibly stupid but it works


