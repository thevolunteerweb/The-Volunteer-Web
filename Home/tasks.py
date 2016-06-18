from celery import Celery
from celery import task
from Requests.models import Volunteer_ngo_request
import datetime
@task
def duplicate(a,b):
    Volunteer_ngo_request.objects.create(sender = a, recepient = b, status = "Accept")
    return "Success"
@task
def sum(a,b):
    return a+b