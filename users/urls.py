from django.conf.urls import *
from users import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="users_index"),
    url(r'^(?P<userID>\d+)/profile/$', views.profile, name="profile"),
    url(r'^(?P<userID>\d+)/resume/$', views.view_resume, name="view_resume"),
    url(r'^(?P<userID>\d+)/sponsor_profile/$', views.sponsor_profile, name="sponsor_profile"),
    url(r'^(?P<userID>\d+)/edit_sponsor_profile/$', views.edit_sponsor_profile, name="edit_sponsor_profile"),
    url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),
    url(r'^admin/', include([
        url(r'^$', views.admin_tools, name="admin_tools"),
        url(r'^sponsors/create/$', views.admin_create_sponsor, name='admin_create_sponsor'),
        url(r'^create/$', views.admin_create_admin, name='admin_create_admin'),
        url(r'^download_csv/$', views.admin_download_csv, name="admin_download_csv"),
        url(r'^edit_officers_page/$', views.admin_edit_officers_page, name="admin_edit_officers_page"),
        ])
    ),
)