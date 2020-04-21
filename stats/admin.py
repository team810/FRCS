from django.contrib import admin
from .models import Game_stats, Pit_stats, Match, Competition

# Register your models here.
admin.site.register(Pit_stats)
admin.site.register(Game_stats)
admin.site.register(Match)
admin.site.register(Competition)