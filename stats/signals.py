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
def create_comp(sender, competition, instance, created, **kwargs):
    if created:
        comp = Competition.objects.get(match_num=instance, competition=competition)
        comp.save()
        
