#-------------------------------------------------------------------------------
# Name:        Request Forms
# Purpose:     Process all request forms
#
# Author:      Siddharth Joshi
#
# Created:     16/03/2016
# Copyright:   (c) admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from django import forms
from Requests.models import Volunteer_ngo_request, Events, Projects, Recurring_request
class Volunteer_ngo_request_form(forms.ModelForm):
    class Meta:
        model = Volunteer_ngo_request
        fields = ('recepient', 'date_vol','time_vol', 'activity', 'vol_duration')
        widgets = {
            'date_vol': forms.DateInput(attrs={'type':'date'}),
        }

class Recurring_request_form(forms.ModelForm):
    class Meta:
        model = Recurring_request
        fields = ('recepient', 'time_vol', 'activity', 'vol_duration', 'startdate_vol', 'enddate_vol', 'frequency')
        widgets = {
            'startdate_vol': forms.DateInput(attrs={'type':'date'}),
            'enddate_vol': forms.DateInput(attrs={'type':'date'}),
        }


class Event_create_form(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('organizer',)
        widgets = {
            'date_vol': forms.DateInput(attrs={'type':'date'}),
        }

class Project_create_form(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('organizer',)
        widgets = {
            'date_vol': forms.DateInput(attrs={'type':'date'}),
        }


class NGOFeedback_form(forms.ModelForm):
    class Meta:
        model = Volunteer_ngo_request
        fields = ('feedback_ngo', 'feedback_ngorating')


class UserFeedback_form(forms.ModelForm):
    class Meta:
        model = Volunteer_ngo_request
        fields = ('feedback_ngo', 'feedback_ngorating')

