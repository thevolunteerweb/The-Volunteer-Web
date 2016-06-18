from django.db import models
import datetime

class Offline_Vol(models.Model):
    date_time_req = models.DateTimeField(auto_now_add=True,null=True)
    ngo_id = models.TextField(max_length = 100, blank = False)
    volunteer_name = models.TextField(max_length = 100, blank = True)
    date_vol = models.DateField(null=True,blank=True)
    time_vol = models.TimeField(blank=True)
    hours_vol = models.PositiveSmallIntegerField()
    activity = models.TextField(max_length = 100, blank = False)

class Offline_Donations(models.Model):
    ngo_id = models.TextField(max_length = 100, blank = False)
    donor_name = models.TextField(max_length = 100, blank = True)
    amount_donated = models.PositiveIntegerField()
    cause = models.TextField(max_length = 1000, blank = True)
    mode_of_payment = models.TextField(default = "Not Specified", max_length = 30)
    date_donated = models.DateField(blank=True,null=True)

class Expenditure (models.Model):
    ngo_id = models.TextField(max_length = 100, blank = False)
    sender = models.TextField(max_length=100, blank = True)
    amount = models.PositiveIntegerField()
    purpose = models.TextField(max_length = 1000, blank = False)
    status = models.TextField(max_length = 240, blank = False, default = "Pending")
    invoice_img = models.ImageField(blank = True)