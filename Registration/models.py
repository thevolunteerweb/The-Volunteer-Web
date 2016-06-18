from django.db import models
from django.contrib.auth.models import User
#from Requests.models import Activity

class NGODomains(models.Model):
    domain=models.TextField(max_length=100,blank=True)

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    #Basic Information
    address = models.TextField(max_length = 100, blank=True)
    #skill levels
    skill_science = models.IntegerField(default = 0)
    skill_math = models.IntegerField(default = 0)
    skill_english = models.IntegerField(default = 0)
    skill_ict = models.IntegerField(default = 0)
    skill_programming = models.IntegerField(default = 0)
    skill_socialmediamarket = models.IntegerField(default = 0)
    skill_sport = models.IntegerField(default = 0)
    interests = models.ManyToManyField(NGODomains)

    def __unicode__(self):
        return self.user.username

#Forms for NGOs registering


class NGOProfile (models.Model):
    #Additional user data fields
    #change blank = True to False once ngo_id hash is set up
    complete=[]
    ngo_id = models.TextField(max_length = 100, blank = True)
    address = models.TextField(max_length = 100, blank=True)
    ngo_name = models.TextField(max_length = 100)
    ngo_description=models.TextField(max_length=200, blank=True)
    ngo_domain=models.IntegerField(blank=True)
    #activity = models.ManyToManyField(Activity)




class NGOEmployeeProfile (models.Model):
    user = models.OneToOneField(User)
    #change blank = True to False once ngo_id hash is set up
    ngo_id = models.TextField(max_length = 100, blank = True)
    #Additional user data fields
    position = models.TextField(blank = False, max_length = 50)
    admin = models.BooleanField(default  = False)
    def __unicode__(self):
        return self.user.username

