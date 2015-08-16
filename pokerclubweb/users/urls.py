from django.conf.urls import *
from users import views

urlpatterns = patterns('',
    url(r'^(?P<userID>\d+)/$', views.profile, name="profile"),
    url(r'^profile/$', views.profile, name="my_profile"),
    url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),
    url(r'^admin/$', views.admin_tools, name="admin_tools"),
)