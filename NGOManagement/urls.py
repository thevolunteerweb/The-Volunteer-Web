#-------------------------------------------------------------------------------
# Name:        URLs for NGO Management App
# Purpose:
#
# Author:      Siddharth Joshi
#
# Created:     15/04/2016
# Copyright:   (c) admin 2016
#-------------------------------------------------------------------------------
from django.conf.urls import url, patterns
from NGOManagement import views

urlpatterns = patterns('',
url(r'^offline-volunteer/', views.offline_volsave, name = "Offline Volunteering Instances"),
url(r'^offline-donations/', views.offline_donationsave, name = "Offline Donations"),
url(r'^expenditure/', views.expendituresave, name = "Expenditure"),
)