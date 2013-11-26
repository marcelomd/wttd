from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'eventex.core.views.home', name='name'),
    url(r'^admin/', include(admin.site.urls)),
)
