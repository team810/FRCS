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
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout-view'),
    path('profile/', views.profile, name = 'profile-view'),
    path('profile-settings/', views.ProfileSettings, name = 'profile-settings-view'),
    path('teamadmin/', views.admin, name = 'admin-view'),
    path('getting-started/', views.gettingStarted, name = 'gettingStarted-view'),
    path('welcome/', views.welcome, name = 'welcome-view'),
    path('guest/', views.guest, name = 'guest-view'),
    path('media/', views.media, name = 'media-view'),
    path('forgot-password/', views.forgot, name = 'forgotPass-view'),
    path('forgot-password/', views.forgot, name = 'forgot-view'),
    path('verify/', views.verify, name = 'verify-view'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
