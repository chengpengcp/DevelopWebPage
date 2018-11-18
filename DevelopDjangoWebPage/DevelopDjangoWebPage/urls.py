"""
Definition of urls for DevelopDjangoWebPage.
"""

from django.conf.urls import include, url
# cp add code 2018118
import HelloworldDjangoApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$',HelloworldDjangoApp.views.index,name="index"),
    url(r'^home$',HelloworldDjangoApp.views.index,name="home"),
    # Examples:
    # url(r'^$', DevelopDjangoWebPage.views.home, name='home'),
    # url(r'^DevelopDjangoWebPage/', include('DevelopDjangoWebPage.DevelopDjangoWebPage.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
