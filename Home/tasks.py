from celery import Celery
from celery import task
from Requests.models import Volunteer_ngo_request
from Registration.models import NGODomains
import datetime
@task
def duplicate(a):
    NGODomains.objects.create(domain = a)
    b=a+"poop"
    return b
@task
def sum(a,b):
    return a+b
