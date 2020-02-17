from django.apps import AppConfig


class StatsConfig(AppConfig):
    name = 'stats'

    def ready(self):
        import stats.signals