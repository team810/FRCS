from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet
from rest_framework.authtoken import views as auth_views

router = DefaultRouter()
router.register("Match", MatchViewSet)


urlpatterns = [
    path('api/docs', views.StatsAPI, name='api-view'),
    path('api/', include(router.urls)),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api-tokn-auth'), 
]
