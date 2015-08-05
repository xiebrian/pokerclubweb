from django.conf.urls import *
from tournaments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="tournaments"),
    url(r'^register/$', views.register, name="register"),
    url(r'^results/$', views.results, name="results"),
)