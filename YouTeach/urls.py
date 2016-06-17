"""YouTeach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Registration import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('Home.urls')),
    url(r'^home/', include('Home.urls')),
    url(r'^request/', include('Requests.urls')),
    url(r'^register/', include('Registration.urls'), name = "Registration"),
    url(r'^login/', views.user_ngo_login, name = "Login"),
    url(r'^logout/', views.user__ngo_logout, name = "Logout"),
    url(r'^manage/', include('NGOManagement.urls'), name = "NGO Management"),

]
