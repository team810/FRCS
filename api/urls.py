from django.urls import include, path
from . import views as api_views
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, UserDetailViewSet, PitViewSet, EmailViewSet, TeamDetailViewset, UserRecordView, ProfileViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token  
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework.authtoken import views




router = DefaultRouter()
router.register("match", MatchViewSet)
router.register("pit", PitViewSet)
router.register("email", EmailViewSet)
router.register("profile", ProfileViewSet)
router.register("users", UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    path('api/team/<team_num>/', api_views.TeamDetailViewset.as_view()),
    path('api/user/<username>/', api_views.UserDetailViewSet.as_view()),
    path('api/userValidate/', api_views.UserRecordView.as_view()),

]
