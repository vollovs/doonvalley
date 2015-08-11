from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<page_slug>\S+)/$', views.detail, name='detail'),
]