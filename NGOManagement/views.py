from django.shortcuts import render, render_to_response
from NGOManagement.forms import Offline_VolForm, Offline_DonationsForm, ExpenditureForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

@login_required
def offline_volsave(request):
     context = RequestContext(request)
     offline_vol = Offline_VolForm()
     saved = False
     if request.method == 'POST': #for processing the form data
        offline_vol = Offline_VolForm(data=request.POST)
        if offline_vol.is_valid():
            offline_vol.save()
            saved = True
        else:
            print offline_vol.errors
     else:
        #set forms blank if there is no HTTP POST
        offline_vol = Offline_VolForm()
     #render template depending on context
     return render_to_response('ngomanagement/offline_vol.html',{'offline_vol': offline_vol, 'saved': saved}, context)

@login_required
def offline_donationsave(request):
     context = RequestContext(request)
     offline_donation = Offline_DonationsForm()
     saved = False
     if request.method == 'POST': #for processing the form data
        offline_donation = Offline_DonationsForm(data=request.POST)
        if offline_volreq.is_valid():
            offline_donation.save()
            saved = True
        else:
            print offline_donation.errors
     else:
        #set forms blank if there is no HTTP POST
        offline_donation = Offline_DonationsForm()
     #render template depending on context
     return render_to_response('ngomanagement/offline_donations.html',{'offline_donation': offline_donation, 'saved': saved}, context)

@login_required
def expendituresave(request):
     context = RequestContext(request)
     expenditure = ExpenditureForm()
     saved = False
     if request.method == 'POST': #for processing the form data
        expenditure = ExpenditureForm(data=request.POST)
        if expenditure.is_valid():
            expenditure.save()
            saved = True
        else:
            print expenditure.errors
     else:
        #set forms blank if there is no HTTP POST
        expenditure = ExpenditureForm()
     #render template depending on context
     return render_to_response('ngomanagement/expenditure.html',{'expenditure': expenditure, 'saved': saved}, context)




