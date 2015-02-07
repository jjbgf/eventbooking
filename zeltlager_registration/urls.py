'''
Created on 07.02.2015

@author: samuelstein
'''

from django.conf.urls import patterns, url

from zeltlager_registration import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)