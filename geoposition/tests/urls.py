from django.conf.urls import patterns, include, path
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    path(r'^$', 'example.views.poi_list'),
    path(r'^admin/', include(admin.site.urls)),
)
