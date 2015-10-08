from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import index_view, protected_view


urlpatterns = patterns('',
    url(r'', include('kompassi_oauth2.urls')),
    url(r'^forms/', include('form_designer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
