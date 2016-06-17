from django.db import models
import datetime

class Activity(models.Model):
    activityname = models.TextField(default = "", max_length = 240)
    skill_science = models.BooleanField(default = False)
    skill_math = models.BooleanField(default = False)
    skill_english = models.BooleanField(default = False)
    skill_ict = models.BooleanField(default = False)
    skill_programming = models.BooleanField(default = False)
    skill_socialmediamarket = models.BooleanField(default = False)
    skill_sport = models.BooleanField(default = False)

class Volunteer_ngo_request(models.Model):
    date_time_req = models.DateTimeField(auto_now_add=True)
    sender = models.TextField(blank = False, max_length = 20)
    recepient = models.TextField(blank = False, max_length = 20)
    date_vol = models.DateField(blank=True)
    time_vol = models.TimeField(blank=True)
    activity = models.TextField(default = "", blank = False, max_length = 240)
    vol_duration = models.IntegerField(default = 0)
    status = models.TextField(blank = False, default = "Pending")
    feedback_user = models.TextField(default = "", blank = True, max_length = 240)
    feedback_ngo = models.TextField(default = "", blank = True, max_length = 240)
    feedback_userrating =  models.IntegerField(default = 0)
    feedback_ngorating =  models.IntegerField(default = 0)
    ngo_complete = models.BooleanField(default = False)
    onetime = models.BooleanField(default = True)

class Recurring_request(models.Model):
    sender = models.TextField(blank = False, max_length = 20)
    recepient = models.TextField(blank = False, max_length = 20)
    startdate_vol = models.DateField(blank = True)
    enddate_vol = models.DateField(blank = True)
    time_vol = models.TimeField(blank = True)
    activity = models.TextField(default = "", blank = False, max_length = 240)
    frequency = models.TextField(default = "", blank = False, max_length = 240)
    date_time_req = models.DateTimeField(auto_now_add=True)
    vol_duration = models.IntegerField(default = 0)
    status = models.TextField(blank = False, default = "Pending")

class Events(models.Model):
    date_time_req = models.DateTimeField(auto_now_add=True)
    event_name = models.TextField(default = "", max_length = 30)
    organizer = models.TextField(blank = False, max_length = 20)
    startdate_vol = models.DateField(blank = True)
    enddate_vol = models.DateField(blank = True)
    starttime_vol = models.TimeField(blank = True)
    endtime_vol = models.TimeField(blank = True)
    activities = models.ManyToManyField(Activity)
    activity_goal = models.TextField(null = True, max_length = 240)
    status = models.TextField(blank = False, default = "Upcoming")

class Projects(models.Model):
    date_time_req = models.DateTimeField(auto_now_add=True)
    project_name = models.TextField(default = "", max_length = 30)
    organizer = models.TextField(blank = False, max_length = 20)
    startdate_vol = models.DateField(blank = True)
    enddate_vol = models.DateField(blank = True)
    starttime_vol = models.TimeField(blank = True)
    endtime_vol = models.TimeField(blank = True)
    activities = models.TextField(default = "", blank = False, max_length = 240)
    status = models.TextField(blank = False, default = "Upcoming")


