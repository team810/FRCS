from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, UserViewSet, PitViewSet
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


router = DefaultRouter()
router.register("Match", MatchViewSet)
router.register("User", UserViewSet)
router.register("Pit", PitViewSet)


urlpatterns = [
    path('api/docs', views.StatsAPI, name='api-view'),
    path('api/', include(router.urls)),
    path('docs/key', views.getKey, name='key-view'),
    path('docs/GET/pit', views.Pit, name='pit-view'),
    path('docs/GET/match', views.Match, name='match-view'),
    path('api/authentication/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('docs/POST/authentication/', views.auth, name='auth-view'),  # <-- And here
    path('docs/errors/', views.errors, name='error-view'),  # <-- And here

]
