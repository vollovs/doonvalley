from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^show/(?P<mid>\S+)/$', views.show_msg, name='show_msg'),
]