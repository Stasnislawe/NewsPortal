from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, upgrade_me, disupgrade_me, IndexView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('index/', IndexView.as_view(), name='index'),
    path('index/upgrade/', upgrade_me, name = 'upgrade'),
    path('index/disupgrade/', disupgrade_me, name = 'disupgrade')
]