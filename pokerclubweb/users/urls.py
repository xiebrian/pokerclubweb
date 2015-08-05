from django.conf.urls import *
from users import views

urlpatterns = patterns('',
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),
)