from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, UserViewSet, PitViewSet
from rest_framework.authtoken.views import obtain_auth_token  
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("Match", MatchViewSet)
router.register("Pit", PitViewSet)
router.register("Users", UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token)

]
