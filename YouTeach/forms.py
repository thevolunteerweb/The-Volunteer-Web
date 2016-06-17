#-------------------------------------------------------------------------------
# Name:        Request Forms
# Purpose:
#
# Author:      Siddharth Joshi
#
# Created:     16/03/2016
#-------------------------------------------------------------------------------
from django import forms
from Requests.models import Volunteer_ngo_request

class Volunteer_ngo_request_form(forms.ModelForm):
    class Meta:
        model = Volunteer_ngo_request
        fields = ('sender', 'recepient', 'date_time', 'additional_details')