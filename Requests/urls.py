#-------------------------------------------------------------------------------
# Name:        Request urls
# Purpose:     Maps all urls for the different types of requests
#
# Author:      Siddharth Joshi
#
# Created:     16/03/2016
#-------------------------------------------------------------------------------
from django.conf.urls import url, patterns
from Requests import views

urlpatterns = patterns('',
url(r'^volunteer/', views.volunteer_request, name = "NGO Volunteership Request"),
)