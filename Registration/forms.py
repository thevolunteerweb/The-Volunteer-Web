#-------------------------------------------------------------------------------
# Name:        User Profile Form
# Purpose:
#
# Author:      Siddharth Joshi
#
# Created:     15/03/2016
#-------------------------------------------------------------------------------
from django import forms
from django.contrib.auth.models import User
from Registration.models import UserProfile, NGOProfile, NGOEmployeeProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('address', 'skill_science', 'skill_english', 'skill_math', 'skill_ict', 'skill_programming', 'skill_sport')

class NGOProfileForm(forms.ModelForm):
    class Meta:
        model = NGOProfile
        fields = ('ngo_name', 'address','ngo_description')

class NGOEmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = NGOEmployeeProfile
        fields = ('id','ngo_id', 'position','admin')

