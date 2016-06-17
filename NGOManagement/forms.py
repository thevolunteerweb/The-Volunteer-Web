#-------------------------------------------------------------------------------
# Name:        NGOManagementForms
# Purpose:
#
# Author:      Siddharth Joshi
#
# Created:     15/03/2016
#-------------------------------------------------------------------------------
from django import forms
from NGOManagement.models import Offline_Vol, Offline_Donations, Expenditure

class Offline_VolForm(forms.ModelForm):
    class Meta:
        model = Offline_Vol
        fields =('ngo_id', 'volunteer_name', 'hours_vol', 'activity', 'date_vol', 'time_vol')

class Offline_DonationsForm(forms.ModelForm):
    class Meta:
        model = Offline_Donations
        fields =('ngo_id', 'donor_name', 'amount_donated', 'cause')

class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields =('ngo_id', 'amount', 'purpose', 'invoice_img')
