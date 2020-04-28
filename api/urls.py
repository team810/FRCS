from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, UserViewSet, PitViewSet
from rest_framework.authtoken.views import obtain_auth_token  
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url


#schema_view = get_schema_view(
#   openapi.Info(
#      title="FRCS API",
#      default_version='v1',
#      description="API for the FRCS crowd sourced data collection site for the FIRST Robotics Competition",
#      terms_of_service="https://www.google.com/policies/terms/",
#      contact=openapi.Contact(email="frcsassistant@gmail.com"),
#      license=openapi.License(name="BSD License"),
#   ),
#   public=True,
#   permission_classes=(permissions.AllowAny,),
#)


router = DefaultRouter()
router.register("Match", MatchViewSet)
router.register("Pit", PitViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    #url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #url(r'^api/schema/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #url(r'^api/docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]
