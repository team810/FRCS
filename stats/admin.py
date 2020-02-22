from django.contrib import admin
from .models import Game_stats, Pit_stats

# Register your models here.
admin.site.register(Pit_stats)
admin.site.register(Game_stats)
