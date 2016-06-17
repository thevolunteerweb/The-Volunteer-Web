#-------------------------------------------------------------------------------
# Name:        URLs for the Home pages
# Author:      Siddharth Joshi
# Created:     14/03/2016
#-------------------------------------------------------------------------------
from django.conf.urls import url, patterns
from Home import views

urlpatterns = patterns('',
url(r'^$', views.general, name = "Homepage"),
url(r'^schedule/', views.schedule, name = "Schedule"),
url(r'^browse/ngos/', views.search, name = "Search"),
url(r'^editprofile/', views.editprofile, name = "Edit Profile"),
url(r'^history/', views.history, name = "History"),
url(r'^volunteer/', views.volunteertable, name = "Volunteer"),
url(r'^ngo/editprofile', views.ngoeditprofile, name = "NGO Edit Profile"),
url(r'^ngo/requests/', views.ngorequest, name = "NGO Requests"),
url(r'^ngo/event/', views.ngoevent, name = "NGO Events and Projects"),
url(r'^ngo/balance/', views.ngobalance, name = "NGO Balance Sheet"),
url(r'^ngo/history/', views.ngohistory, name = "NGO History"),

)