from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import UuskairaView, logout_view


urlpatterns = patterns('',
    url(r'', include('kompassi_oauth2.urls')),
    url(r'^$', UuskairaView.as_view(template_name='index.jade'), name='index_view'),
    url(r'^error/?$', UuskairaView.as_view(template_name='login_error.jade'), name='login_error_view'),
    url(r'^forms/', include('form_designer.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/?$', logout_view, name='logout_view'),
)
