from django.conf.urls import *
from tournaments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="tournaments"),
    url(r'^admin/create$', views.admin_create, name="admin_create"),
    url(r'^(?P<tournamentID>\d+)/', include([
        url(r'^$', views.summary, name="summary"),
        url(r'^register/$', views.register, name="register"),
        url(r'^results/$', views.results, name="results"),
        url(r'^admin/results$', views.admin_results, name="admin_results"),
        url(r'^admin/edit$', views.admin_create, name="admin_edit"),
    ])),
)