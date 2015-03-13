from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventbooking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^zeltlager/', include('zeltlager_registration.urls')),
    (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {'document_root': settings.STATIC_ROOT}),
)


