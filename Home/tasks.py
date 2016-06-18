from celery import Celery
from celery import task
from Requests.models import Volunteer_ngo_request
from Registration.models import NGODomains
import datetime
@task
def duplicate(a):
    NGODomains.objects.create(domain = a)
    return "Success"
@task
def sum(a,b):
    return a+b
