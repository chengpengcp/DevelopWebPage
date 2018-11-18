"""
Definition of urls for DevelopDjangoWebPage.
"""

from django.conf.urls import include, url
import HelloworldDjangoApp.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', HelloworldDjangoApp.views.index, name='index'),
    url(r'^home$', HelloworldDjangoApp.views.index, name='home'),
]