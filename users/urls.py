from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from DjangoFRCS import settings

urlpatterns = [
    path('', views.index, name = 'home-view'),
    path('login/', views.login, name = 'login-view'),
    path('register/', views.register, name = 'register-view'),
    path('scout/', views.scout, name = 'scout-view'),
    path('pitscout/', views.Pitscout, name = 'Pitscout-view'),
    path('scouthub/', views.scouthub, name = 'ScoutHub-view'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout-view'),
    path('profile/', views.profile, name = 'profile-view'),
    path('profile-settings/', views.ProfileSettings, name = 'profile-settings-view'),
    path('teamadmin/', views.admin, name = 'admin-view'),
    path('gettingStarted/', views.gettingStarted, name = 'gettingStarted-view'),
    path('welcome/', views.welcome, name = 'welcome-view'),
    path('guest/', views.guest, name = 'guest-view'),
    path('media/', views.media, name = 'media-view'),
    path('forgotPassword/', views.forgot, name = 'forgotPass-view'),
    path('pitData/', views.pitdata, name = 'pitdata-view'),
    path('gameData/', views.gamedata, name = 'gamedata-view'),
    path('feed/', views.feed, name = 'feed-view')




]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
