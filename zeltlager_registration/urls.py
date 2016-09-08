'''
Created on 07.02.2015

@author: samuelstein
'''

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from zeltlager_registration import views

urlpatterns = ['',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^save/$', views.save, name='save'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)