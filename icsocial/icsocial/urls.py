from django.conf.urls import patterns, include, url
from views import login,place
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'icsocial.views.home', name='home'),
    url(r'^login/', login),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	)
