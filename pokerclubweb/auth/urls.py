from django.conf.urls import *
from auth import views

urlpatterns = patterns('',
    url(r'^login/$', views.login, name="login"),
    url(r'^signup/$', views.signup, name="signup"),
)