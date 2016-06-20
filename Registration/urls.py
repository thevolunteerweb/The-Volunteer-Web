#-------------------------------------------------------------------------------
# Name:        Login Urls
# Purpose:
#
# Author:      Siddharth Joshi
#-------------------------------------------------------------------------------

from django.conf.urls import url, patterns
from Registration import views

urlpatterns = patterns('',
url(r'^individual/', views.user_register, name = "Indivdual Registration"),
url(r'^ngo/', views.ngo_register, name = "NGO Registration"),
url(r'^profile/', views.update_profile, name = "Profile update"),
url(r'^ngoprofile/', views.update_ngoprofile, name = "NGO Profile update"),
url(r'^ngoemployee/', views.ngoemp_register, name = "NGO Employee Register"),
)