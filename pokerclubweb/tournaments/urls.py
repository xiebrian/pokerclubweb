from django.conf.urls import *
from tournaments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="tournaments"),
    url(r'^register/$', views.register, name="register"),
    url(r'^results/$', views.results, name="results"),
    url(r'^admin/create$', views.admin_create, name="admin_create"),
    url(r'^admin/(?P<tournamentID>\d+)/results$', views.admin_results, name="admin_results"),
)