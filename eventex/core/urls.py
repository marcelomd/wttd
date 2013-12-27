# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.core.views',
        url(r'^palestrantes/(?P<slug>[\w-]+)/$', 'speaker_detail', name='speaker_detail'),
        url(r'^palestras/(?P<pk>\d+)/$', 'talk_detail', name='talk_detail'),
        url(r'^palestras/$', 'talk_list', name='talk_list'),
        url(r'^$', 'home', name='home'),
)
