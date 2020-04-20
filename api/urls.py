from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet

router = DefaultRouter()
router.register("Match", MatchViewSet)


urlpatterns = [
    path('api/docs', views.StatsAPI, name='api-view'),
    path('api/', include(router.urls)),
]
