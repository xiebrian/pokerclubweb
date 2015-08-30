from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from filebrowser.sites import site as fb_site
from frontend.views import TextFileView, Http500View
from pokerclubweb import views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.views.generic import RedirectView

admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}

urlpatterns = patterns('',
    # Django admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(fb_site.urls)),
    url(r'^admin/util/tools/', include('admin_tools.urls')),

    # Test pages
    url(r'^500test/$', view=Http500View.as_view()),
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),

    # SEO API's
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots.txt$', TextFileView.as_view(content_type='text/plain', template_name='robots.txt')),

    # Monitoring API's
    url(r'^api/ping/', include('ping.urls')),

    # allauth
    url(r'^accounts/', include('allauth.urls')),

    # CMS modules
    url(r'^$', views.index, name="index"),
    url(r'^about/', views.about, name="about"),
    url(r'^events/', views.events, name="events"),
    url(r'^sponsors/', views.sponsors, name="sponsors"),
    url(r'^officers/', views.officers, name="officers"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^photos/', views.photos, name="photos"),
    url(r'^auth/', include([
        url(r'^login/$', views.login, name="login"),
        url(r'^logout/$', views.logout, name="logout"),
        url(r'^signup/$', views.signup, name="signup"),
        url(r'^change_password/$', views.change_password, name="change_password"),
        url(r'^change_password_done/$', views.change_password_done, name="password_change_done"),
        url(r'^reset_password/$', views.reset_password, name="reset_password"),
        url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_password_confirm, name="password_reset_confirm"),
        url(r'^reset_password_done/$', views.reset_password_done, name="password_reset_done"),
        url(r'^reset_password_complete/$', views.reset_password_complete, name="password_reset_complete"),
        ])
    ),
    url(r'^users/', include('users.urls')),
    url(r'^tournaments/', include('tournaments.urls')),

    url(r'^media/resumes/(?P<userID>\d+)/', RedirectView.as_view(pattern_name="view_resume", permanent=False)),
)

if settings.DEBUG:
    urlpatterns.append(
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )
