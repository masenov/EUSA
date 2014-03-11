from django.conf.urls import patterns, url
from django.views.generic import ListView

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'write/$', views.create),
    url(r'thankyou/$', views.thankyou, name='thankyou'),
)
