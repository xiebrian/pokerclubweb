from django.conf.urls import *
from tournaments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="tournaments"),
    url(r'^admin/create$', views.admin_create_tournament, name="admin_create_tournament"),
    url(r'^(?P<tournamentID>\d+)/', include([
        url(r'^$', views.summary, name="summary"),
        url(r'^register/$', views.register, name="register"),
        url(r'^results/$', views.results, name="results"),
        url(r'^admin/results$', views.admin_edit_tournament_results, name="admin_edit_tournament_results"),
        url(r'^admin/edit$', views.admin_create_tournament, name="admin_edit_tournament"),
    ])),
)