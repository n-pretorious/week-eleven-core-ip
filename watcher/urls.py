from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('hood', views.index, name='index'),
    path('profile', views.profile, name='userProfile'),
    path('business', views.business, name='registerBusiness')
]