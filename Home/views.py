from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q
import datetime
from tasks import duplicate
from Registration.models import User, UserProfile, NGOProfile, NGODomains, NGOEmployeeProfile, Activity
from Registration.forms import UserForm
from NGOManagement.models import Offline_Vol, Offline_Donations,Expenditure
from NGOManagement.forms import Offline_VolForm, Offline_DonationsForm, ExpenditureForm
from Requests.models import Volunteer_ngo_request, Events, Projects, Recurring_request
from Requests.forms import Volunteer_ngo_request_form, NGOFeedback_form, UserFeedback_form
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
import os
from random import randint

quotes=["Education is the most powerful weapon which you can use to change the world.","Education is not preparation for life; education is life itself.","Education's purpose is to replace an empty mind with an open one.","The whole purpose of education is to turn mirrors into windows.","Education is not the filling of a pail, but the lighting of a fire."]
pers=["Nelson Mandela","John Dewey","Malcolm Forbes","Sydney J. Harris","William Butler Yeats"]
profile_data = {}

def general(request):
    if(request.method == 'POST'):
        dec=request.POST.get('dec')
        if dec=="User Complete":
            if Volunteer_ngo_request.objects.get(id = request.POST.get('id')) == "NGO Complete":
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status="Completed")
            else:
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status=dec)
            return HttpResponse('User Completed',content_type="application/text")

        elif dec=="User Abort":
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status=dec)
                return HttpResponse('User Aborted',content_type="application/text")

        elif dec=="NGO Complete":
            if Volunteer_ngo_request.objects.get(id = request.POST.get('id')) == "User Complete":
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status="Completed")
            else:
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status=dec)
            return HttpResponse('NGO Completed',content_type="application/text")

        elif dec=="NGO Abort":
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status=dec)
                return HttpResponse('Aborted',content_type="application/text")

        elif dec=="Accept":
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status=dec)
                return HttpResponse('Accepted', content_type="application/text")
        elif dec=="Reject":
                Volunteer_ngo_request.objects.filter(id = request.POST.get('id')).update(status=dec)
                return HttpResponse('Rejected',content_type="application/text")

        elif dec=="Accept Recurring":
               Recurring_request.objects.filter(id = request.POST.get('id')).update(status=dec)
               recur_request = Recurring_request.objects.get(id = request.POST.get('id'))
               if recur_request.frequency == "Daily":
                    new_reqdatetime = datetime.datetime.combine(recur_request.startdate_vol, recur_request.time_vol)
                    while(new_reqdatetime.date() <= recur_request.enddate_vol):
                        duplicate.apply_async(eta = new_reqdatetime - datetime.timedelta(days = 1), args = [recur_request.sender, recur_request.recepient, new_reqdatetime.date() , recur_request.time_vol, recur_request.activity])
                        new_reqdatetime += datetime.timedelta(days = 1)

               elif recur_request.frequency == "Weekly":
                    new_reqdatetime = datetime.datetime.combine(recur_request.startdate_vol, recur_request.time_vol)
                    while(new_reqdatetime.date() <= recur_request.enddate_vol):
                        duplicate.apply_async(eta = new_reqdatetime - datetime.timedelta(days = 3), args = [recur_request.sender, recur_request.recepient, new_reqdatetime.date() , recur_request.time_vol, recur_request.activity])
                        new_reqdatetime += datetime.timedelta(days = 7)

               elif recur_request.frequency == "Fortnightly":
                    new_reqdatetime = datetime.datetime.combine(recur_request.startdate_vol, recur_request.time_vol)
                    while(new_reqdatetime.date() <= recur_request.enddate_vol):
                        duplicate.apply_async(eta = new_reqdatetime - datetime.timedelta(days = 3), args = [recur_request.sender, recur_request.recepient, new_reqdatetime.date() , recur_request.time_vol, recur_request.activity])
                        new_reqdatetime += datetime.timedelta(days = 15)

               elif recur_request.frequency == "Monthly":
                    new_reqdatetime = datetime.datetime.combine(recur_request.startdate_vol, recur_request.time_vol)
                    while(new_reqdatetime.date() <= recur_request.enddate_vol):
                        duplicate.apply_async(eta = new_reqdatetime - datetime.timedelta(days = 3), args = [recur_request.sender, recur_request.recepient, new_reqdatetime.date() , recur_request.time_vol, recur_request.activity])
                        new_reqdatetime += datetime.timedelta(days = 30)

               return HttpResponse('Recurring Accepted', content_type="application/text")

        elif dec=="Reject Recurring":
                Recurring_request.objects.filter(id = request.POST.get('id')).update(status=dec)
                return HttpResponse('Recurring Rejected',content_type="application/text")

        elif dec=="Approved":
               Expenditure.objects.filter(ngo_id = NGOEmployeeProfile.objects.get(user_id = user_id.id).ngo_id).update(status=dec)
               return HttpResponse('Approved', content_type="application/text")
        elif dec=="Denied":
                Expenditure.objects.filter(ngo_id = NGOEmployeeProfile.objects.get(user_id = user_id.id).ngo_id).update(status=dec)
                return HttpResponse('Denied', content_type="application/text")


    else:
        context = RequestContext(request)

        profile_data['is_requests'] = True
        profile_data['is_member']=False
        profile_data['is_ngo'] = False
        profile_data['is_user'] = False
        try:
            user_id = User.objects.get(username = request.session['username'])

            profile_data['is_member'] = True
        except:
            pass
        try:
            profile_id = NGOProfile.objects.get(ngo_id = user_id.id)
            profile_data['is_ngo'] = True
        except:
            try:
                profile_id = UserProfile.objects.get(user_id = user_id.id)
                profile_data['is_user'] = True
            except:
                pass

        if profile_data['is_user']:
            profile_data['name'] = user_id.first_name
            hours_count_requests = Volunteer_ngo_request.objects.filter(sender = user_id.id)
            profile_data['hours_vol'] = 0
            for req in hours_count_requests:
                profile_data['hours_vol'] += req.vol_duration
            context=RequestContext(request)
            return render_to_response('home/user/feed.html', profile_data, context)

        elif profile_data['is_ngo']:
            profile_data['name'] = user_id.first_name
            hours_count_requests = Volunteer_ngo_request.objects.filter(recepient = user_id.id)
            profile_data['hours_vol'] = 0
            for req in hours_count_requests:
                profile_data['hours_vol'] += req.vol_duration

            offline_vols = Offline_Vol.objects.filter(ngo_id = user_id.id)
            profile_data['offlinehours_vol'] = 0
            for req in offline_vols:
                profile_data['offlinehours_vol'] += req.hours_vol

            expenses = Expenditure.objects.filter(ngo_id = user_id.id)
            profile_data['total_expenditure'] = 0
            for req in expenses:
                profile_data['total_expenditure'] += req.amount

            donations = Offline_Donations.objects.filter(ngo_id = user_id.id)
            profile_data['total_donation'] = 0
            for req in donations:
                profile_data['total_donation'] += req.amount_donated


            context = RequestContext(request)
            return render_to_response('home/ngo/ngofeed.html', profile_data, context)
        else:
            profile_data['totalhours_vol'] = 0
            hours_count_requests = Volunteer_ngo_request.objects.filter()
            for req in hours_count_requests:
                profile_data['totalhours_vol'] += req.vol_duration
            profile_data['total_users'] = User.objects.filter().count()
            profile_data['total_ngos'] = NGOProfile.objects.filter().count()
            profile_data['user_form'] = UserForm()
        return render_to_response('home/home.html', profile_data, context)

@login_required
def schedule(request):
    context = RequestContext(request)
    user_id = User.objects.get(username = request.session['username'])
    schedule_data = {}
    scheduled_requests = Volunteer_ngo_request.objects.filter(Q(sender =user_id.id , status = "Accept") | Q(recepient = user_id.id, status = "Accept"))
    if len(scheduled_requests) == 0:
        schedule_data['is_requests'] = False
    else:
        schedule_data['is_requests'] = True
        for req in scheduled_requests:
            #converts date time to required format
            req.date_time_vol = (req.date_time_vol - datetime.datetime(1970,1,1)).total_seconds()*1000
            req.vol_duration = req.date_time_vol + req.vol_duration * 3600 * 1000
            ngo_id =  User.objects.get(username = req.recepient)
            ngo_profile_id = NGOProfile.objects.get(user = ngo_id)
            req.name = ngo_profile_id.ngo_name
        schedule_data['requests'] = scheduled_requests

    schedule_data['is_ngo'] = False
    schedule_data['is_user'] = False

    try:
        user_id = User.objects.get(username = request.session['username'])
        profile_id = UserProfile.objects.get(user = user_id)
        schedule_data['name'] = profile_id.first_name
        schedule_data['is_user'] = True
    except:
        try:
            profile_id = NGOProfile.objects.get(user = user_id)
            schedule_data['name'] = profile_id.ngo_name
            schedule_data['is_ngo'] = True
        except:
            pass

    return render_to_response('home/schedule.html', schedule_data, context)

@login_required
def search(request):
    resp={}
    user_id = User.objects.get(username = request.session['username'])
    resp['name'] = user_id.first_name
    a=""
    context = RequestContext(request)
    if(request.method =="POST"):
        a=request.POST.get('term')
        result=[]
        res=list(NGOProfile.objects.filter(ngo_name__istartswith=a))

        for i in res:
            temp={}
            temp['ngo_name']=i.ngo_name
            temp['name']=""
            temp['ngo_id']=i.ngo_id
            temp['address']=i.address
            temp['ngo_domain']=NGODomains.objects.get(id=i.ngo_domain).domain
            temp['ngo_description']=i.ngo_description
            temp['activity']=[]
            for x in i.activity.filter():
                temp['activity'].append(x.activityname)
            temp['type']='NGO'
            result.append(temp)
        res=list(Events.objects.filter(organizer__istartswith=a))
        for i in res:
            temp={}
            temp['ngo_name']=i.event_name
            temp['name']=NGOProfile.objects.get(ngo_id=i.organizer).ngo_name
            temp['ngo_id']=i.id
            temp['address']=NGOProfile.objects.get(ngo_id=i.organizer).address
            temp['ngo_domain']=NGODomains.objects.get(id=NGOProfile.objects.get(ngo_id=i.organizer).ngo_domain).domain
            temp['ngo_description']=i.event_description
            temp['activity']=[]
            for x in i.activities.filter():
                temp['activity'].append(x.activityname)
            temp['type']='Event'
            result.append(temp)
        res=list(Projects.objects.filter(organizer__istartswith=a))
        for i in res:
            temp={}
            temp['ngo_name']=i.project_name
            temp['name']=NGOProfile.objects.get(ngo_id=i.organizer).ngo_name
            temp['ngo_id']=i.id
            temp['address']=NGOProfile.objects.get(ngo_id=i.organizer).address
            temp['ngo_domain']=NGODomains.objects.get(id=NGOProfile.objects.get(ngo_id=i.organizer).ngo_domain).domain
            temp['ngo_description']=i.project_description
            temp['activity']=[]
            for x in i.activities.filter():
                temp['activity'].append(x.activityname)
            temp['type']='Project'
            result.append(temp)
        if len(result)==0:
            return HttpResponse("None")
        else:
            result=json.dumps(result)
            return HttpResponse(result,content_type="application/json")
    return render_to_response('home/user/ngobrowse.html',resp,context)

@login_required
def history(request):
    user_id = User.objects.get(username = request.session['username'])
    profile_data['name'] = user_id.first_name
    context = RequestContext(request)

    profile_data['is_user_cancelrequests'] = True
    profile_data['usercancel_requests'] = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status = "User Abort"))
    if len(profile_data['usercancel_requests']) == 0:
        profile_data['is_user_cancelrequests'] = False

    profile_data['is_ngo_cancelrequests'] = True
    profile_data['ngocancel_requests'] = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status = "NGO Abort"))
    if len(profile_data['ngocancel_requests']) == 0:
        profile_data['is_ngo_cancelrequests'] = False

    profile_data['is_completedrequests'] = True
    profile_data['completed_requests'] = list(Volunteer_ngo_request.objects.filter(Q(sender =user_id.id , status = "User Complete") | Q(sender = user_id.id, status = "Completed")))
    if len(profile_data['completed_requests']) == 0:
        profile_data['is_completedrequests'] = False

    profile_data['is_rejectedrequests'] = True
    profile_data['rejected_requests'] = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status = "Reject"))
    if len(profile_data['rejected_requests']) == 0:
        profile_data['is_rejectedrequests'] = False

    return render_to_response('home/user/history.html', profile_data, context)


@login_required
def volunteertable(request):
    user_id = User.objects.get(username = request.session['username'])
    profile_data['name'] = user_id.first_name
    context = RequestContext(request)
    if(request.method == 'POST'):
        a=Volunteer_ngo_request.objects.filter(id=request.POST.get('id')).update(feedback_user=request.POST.get('feedback_user'),feedback_userrating=request.POST.get('feedback_userrating'))
        return HttpResponse('User Completed', content_type="application/text")
    else:
        feedback_form = UserFeedback_form()
        profile_data['is_upcomingrequests'] = True
        profile_data['is_ongoingrequests'] = True
        profile_data['upcoming_requests'] = list()
        profile_data['ongoing_requests'] = list()
        requests = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status ="Accept", req_type = "NGO"))
        for req in requests:
            if req.date_vol > datetime.date.today():
                profile_data['upcoming_requests'].append(req)
            elif req.date_vol == datetime.date.today() and req.time_vol > datetime.datetime.now().time():
                profile_data['upcoming_requests'].append(req)
            else:
                 profile_data['ongoing_requests'].append(req)

        requests = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status ="Accept", req_type = "Event"))
        for req in requests:
            if req.date_vol > datetime.date.today():
                profile_data['event_upcoming_requests'].append(req)
            elif req.date_vol == datetime.date.today() and req.time_vol > datetime.datetime.now().time():
                profile_data['event_upcoming_requests'].append(req)
            else:
                 profile_data['event_ongoing_requests'].append(req)

        requests = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status ="Accept", req_type = "Project"))
        for req in requests:
            if req.date_vol > datetime.date.today():
                profile_data['project_upcoming_requests'].append(req)
            elif req.date_vol == datetime.date.today() and req.time_vol > datetime.datetime.now().time():
                profile_data['project_upcoming_requests'].append(req)
            else:
                 profile_data['project_ongoing_requests'].append(req)

        ngo_completed = list(Volunteer_ngo_request.objects.filter(sender =user_id.id , status = "NGO Complete", req_type = "NGO"))
        for req in ngo_completed:
            profile_data['ongoing_requests'].append(req)

        ngo_completed = list(Volunteer_ngo_request.objects.filter(sender =user_id.id , status = "NGO Complete", req_type = "Event"))
        for req in ngo_completed:
            profile_data['event_ongoing_requests'].append(req)

        ngo_completed = list(Volunteer_ngo_request.objects.filter(sender =user_id.id , status = "NGO Complete", req_type = "Project"))
        for req in ngo_completed:
            profile_data['project_ongoing_requests'].append(req)

        if len(profile_data['upcoming_requests']) == 0 & len(profile_data['event_upcoming_requests']) == 0 & len(profile_data['event_upcoming_requests']) == 0:
            profile_data['is_upcomingrequests'] = False
        else:
            for req in profile_data['upcoming_requests']:
                    req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name
            for req in profile_data['event_upcoming_requests']:
                    req.recepient=Events.objects.get(id=req.recepient).event_name
            for req in profile_data['project_upcoming_requests']:
                    req.recepient=Projects.objects.get(id=req.recepient).project_name

        if len(profile_data['ongoing_requests']) == 0 & len(profile_data['event_ongoing_requests']) == 0 & len(profile_data['event_ongoing_requests']) == 0:
            profile_data['is_ongoingrequests'] = False
        else:
            for req in profile_data['ongoing_requests']:
                    req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name
            for req in profile_data['event_ongoing_requests']:
                    req.recepient=Events.objects.get(id=req.recepient).event_name
            for req in profile_data['project_ongoing_requests']:
                    req.recepient=Projects.objects.get(id=req.recepient).project_name


        profile_data['is_pendingrequests'] = True
        profile_data['pending_requests'] = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status ="Pending"))
        if len(profile_data['pending_requests']) == 0:
            profile_data['is_pendingrequests'] = False
        else:
            for req in profile_data['pending_requests']:
                    req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name

        profile_data['is_recur_pendingrequests'] = True
        profile_data['recur_pending_requests'] = list(Recurring_request.objects.filter(sender = user_id.id, status ="Pending"))
        if len(profile_data['recur_pending_requests']) == 0:
            profile_data['is_recur_pendingrequests'] = False
        else:
            for req in profile_data['recur_pending_requests']:
                    req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name

        return render_to_response('home/user/requests.html', profile_data, context)

@login_required
def history(request):
    user_id = User.objects.get(username = request.session['username'])
    profile_data['name'] = user_id.first_name
    context = RequestContext(request)

    profile_data['is_ngo_cancelrequests'] = True
    profile_data['ngocancel_requests'] = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status = "NGO Abort"))
    if len(profile_data['ngocancel_requests']) == 0:
        profile_data['is_ngo_cancelrequests'] = False
    else:
        for req in profile_data['ngocancel_requests']:
            req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name
    profile_data['is_completedrequests'] = True
    profile_data['completed_requests'] = list(Volunteer_ngo_request.objects.filter(Q(sender =user_id.id , status = "User Complete") | Q(sender = user_id.id, status = "Completed")))
    if len(profile_data['completed_requests']) == 0:
        profile_data['is_completedrequests'] = False
    else:
        for req in profile_data['completed_requests']:
            req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name
    profile_data['is_rejectedrequests'] = True
    profile_data['rejected_requests'] = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status = "Reject"))
    if len(profile_data['rejected_requests']) == 0:
        profile_data['rejected_requests'] = False
    else:
        for req in profile_data['rejected_requests']:
            req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name
    profile_data['is_user_cancelrequests'] = True
    profile_data['usercancel_requests'] = list(Volunteer_ngo_request.objects.filter(sender = user_id.id, status = "User Abort"))
    if len(profile_data['usercancel_requests']) == 0:
        profile_data['is_user_cancelrequests'] = False
    else:
        for req in profile_data['usercancel_requests']:
            req.recepient=NGOProfile.objects.get(ngo_id=req.recepient).ngo_name
    return render_to_response('home/user/history.html', profile_data, context)


@login_required
def editprofile(request):
    user_id = User.objects.get(username = request.session['username'])
    profile_data['name'] = user_id.first_name
    context = RequestContext(request)

    profile_data['skillmath'] = UserProfile.objects.get(user = user_id).skill_math
    profile_data['skillict'] = UserProfile.objects.get(user = user_id).skill_ict
    profile_data['skillmarket'] = UserProfile.objects.get(user = user_id).skill_socialmediamarket
    profile_data['skillscience'] = UserProfile.objects.get(user = user_id).skill_science
    profile_data['skillenglish'] = UserProfile.objects.get(user = user_id).skill_english
    profile_data['skillsport'] = UserProfile.objects.get(user = user_id).skill_sport
    profile_data['skillprog'] = UserProfile.objects.get(user = user_id).skill_programming
    profile_data['about'] = UserProfile.objects.get(user = user_id).bio
    profile_data['address'] = UserProfile.objects.get(user = user_id).address

    if request.method == 'POST':
       UserProfile.objects.filter(user = user_id).update(bio=request.POST.get('about'),address=request.POST.get('address'),skill_math = request.POST.get('math'),skill_ict = request.POST.get('ict'),skill_science = request.POST.get('science'),skill_programming = request.POST.get('programming'),skill_english = request.POST.get('english'),skill_sport = request.POST.get('sport'),skill_socialmediamarket = request.POST.get('marketing'))
       return HttpResponseRedirect("/home/editprofile")

    return render_to_response('home/user/editprofile.html', profile_data, context)


@login_required
def ngoeditprofile(request):
    data = {}
    user_id = User.objects.get(username = request.session['username'])
    data['name'] = user_id.first_name
    context = RequestContext(request)
    return render_to_response('home/ngo/ngoprofile.html', data, context)

@login_required
def ngohistory(request):
    user_id = User.objects.get(username = request.session['username'])
    profile_data['name'] = user_id.first_name
    context = RequestContext(request)

    profile_data['is_user_cancelrequests'] = True
    profile_data['usercancel_requests'] = list(Volunteer_ngo_request.objects.filter(recepient = user_id.id, status = "User Abort"))
    if len(profile_data['usercancel_requests']) == 0:
        profile_data['is_user_cancelrequests'] = False

    profile_data['is_ngo_cancelrequests'] = True
    profile_data['ngocancel_requests'] = list(Volunteer_ngo_request.objects.filter(recepient = user_id.id, status = "NGO Abort"))
    if len(profile_data['ngocancel_requests']) == 0:
        profile_data['is_ngo_cancelrequests'] = False

    profile_data['is_completedrequests'] = True
    profile_data['completed_requests'] = list(Volunteer_ngo_request.objects.filter(Q(recepient =user_id.id , status = "NGO Complete") | Q(recepient = user_id.id, status = "Completed")))
    if len(profile_data['completed_requests']) == 0:
        profile_data['is_completedrequests'] = False

    profile_data['is_rejectedrequests'] = True
    profile_data['rejected_requests'] = list(Volunteer_ngo_request.objects.filter(recepient = user_id.id, status = "Reject"))
    if len(profile_data['rejected_requests']) == 0:
        profile_data['is_rejectedrequests'] = False

    return render_to_response('home/ngo/ngohistory.html', profile_data, context)

@login_required
def ngobalance(request):
    user_obj = User.objects.get(username = request.session['username'])
    profile_data['name'] = user_obj.first_name
    context = RequestContext(request)
    if(request.method == 'POST'):
        if(request.POST.get('input_type')=="offline_vol"):
            a=Offline_Vol.objects.create(ngo_id=user_obj.id,volunteer_name=request.POST.get('volunteer_name'),activity=request.POST.get('activity'),hours_vol=request.POST.get('hours_vol'),date_vol=request.POST.get('date_vol'),time_vol=request.POST.get('time_vol'))
            return HttpResponse('Offline Volunteering Request Inputted', content_type="application/text")
        elif(request.POST.get('input_type')=="offline_donations"):
            a=Offline_Donations.objects.create(ngo_id=user_obj.id,donor_name=request.POST.get('donor_name'),mode_of_payment=request.POST.get('mode_of_payment'),amount_donated=request.POST.get('amount_donated'),date_donated=request.POST.get('date_donated'),cause=request.POST.get('cause'))
            return HttpResponse('Offline Donation Logged', content_type="application/text")
        elif(request.POST.get('input_type')=="expenditure"):
            a=Expenditure.objects.create(ngo_id = NGOEmployeeProfile.objects.get(user_id = user_obj.id).ngo_id, sender=user_obj.id, purpose=request.POST.get('purpose'), amount=request.POST.get('amount'))
            return HttpResponse('Expense Inputted', content_type="application/text")
    else:
        #Loading offline volunteering instances that are in the databse for viewing
         profile_data['is_offlinevols'] = True
         profile_data['offline_vols'] = list(Offline_Vol.objects.filter(ngo_id = user_obj.id))
         if len(profile_data['offline_vols']) == 0:
            profile_data['is_offlinevols'] = False
         else:
            max = 0
            profile_data['total_offline_volhours'] = 0
            for vol in profile_data['offline_vols']:
                if (max < vol.hours_vol):
                     profile_data['top_volunteer'] = vol.volunteer_name
                     max =  vol.hours_vol
                profile_data['total_offline_volhours'] += vol.hours_vol



        #Loading donations that are in the databse for viewing
         profile_data['is_offlinedonations'] = True
         profile_data['offline_donations'] = list(Offline_Donations.objects.filter(ngo_id = user_obj.id))
         if len(profile_data['offline_donations']) == 0:
           profile_data['is_offlinedonations'] = False
         else:
           max = 0
           profile_data['total_offline_donation'] = 0
           for vol in profile_data['offline_donations']:
               profile_data['total_offline_donation'] += vol.amount_donated
               if (max < vol.amount_donated):
                    profile_data['top_donor'] = vol.donor_name
                    max = vol.amount_donated

        #Loading expenses pending approval for viewing and approving
         profile_data['is_pendingexpenses'] = True
         profile_data['pending_expenses'] = list(Expenditure.objects.filter(ngo_id = NGOEmployeeProfile.objects.get(user_id = user_obj.id).ngo_id, status = "Pending"))
         if len(profile_data['pending_expenses']) == 0:
           profile_data['is_pendingexpenses'] = True
         else:
            for vol in profile_data['pending_expenses']:
                vol.sender = User.objects.get(id = user_obj.id).username

        #Loading past expenses for viewing
         profile_data['is_pastexpenses'] = True
         profile_data['past_expenses'] = list(Expenditure.objects.filter((Q(ngo_id =NGOEmployeeProfile.objects.get(user_id = user_obj.id).ngo_id , status = "Approved") | Q(ngo_id = NGOEmployeeProfile.objects.get(user_id = user_obj.id).ngo_id, status = "Denied"))))
         if len(profile_data['past_expenses']) == 0:
           profile_data['is_pastexpenses'] = True
         else:
            profile_data['total_expenditure'] = 0
            for vol in profile_data['past_expenses']:
                vol.sender = User.objects.get(id = user_obj.id).username
                profile_data['total_expenditure'] += vol.amount
            profile_data['net_income'] = profile_data['total_offline_donation']-profile_data['total_expenditure']

    return render_to_response('home/ngo/ngobalance.html', profile_data, context)


@login_required
@login_required
def ngoevent(request):
    data = {}
    user_id = User.objects.get(username = request.session['username'])
    data['name'] = user_id.first_name
    data['array']=list(Activity.objects.filter())
    context = RequestContext(request)
    if request.method=='POST':
        if request.POST.get('type')=='event':
            a=Events.objects.create(event_name=request.POST.get('event_name'),organizer=user_id.id,startdate_vol=request.POST.get('startdate_vol'),enddate_vol=request.POST.get('enddate_vol'),starttime_vol=request.POST.get('starttime_vol'),endtime_vol=request.POST.get('endtime_vol'))
            b={}
            for ind,x in enumerate(request.POST.getlist('activities[]')):
                a.activities.add(Activity.objects.get(activityname=x))
                b[str(x)]=int(request.POST.getlist('activity_goal[]')[ind])
            b=json.dumps(b)
            Events.objects.filter(id=a.id).update(activity_goal=b)
            return HttpResponse(b,content_type="application/text")
        if request.POST.get('type')=='project':
            a=Projects.objects.create(project_name=request.POST.get('project_name'),organizer=user_id.id,startdate_vol=request.POST.get('startdate_vol'),enddate_vol=request.POST.get('enddate_vol'),starttime_vol=request.POST.get('starttime_vol'),endtime_vol=request.POST.get('endtime_vol'))
            b={}
            for ind,x in enumerate(request.POST.getlist('activities[]')):
                a.activities.add(Activity.objects.get(activityname=x))
                b[str(x)]=int(request.POST.getlist('activity_goal[]')[ind])
            b=json.dumps(b)
            Events.objects.filter(id=a.id).update(activity_goal=b)
            return HttpResponse(b,content_type="application/text")

        else:
            return HttpResponse("Failed",content_type="application/text")
    else:
        return render_to_response('home/ngo/ngoevent.html', data, context)


@login_required
def ngorequest(request):
    if(request.method == 'POST'):
        a=Volunteer_ngo_request.objects.filter(id=request.POST.get('id')).update(feedback_ngo=request.POST.get('feedback_ngo'),feedback_ngorating=request.POST.get('feedback_ngorating'))
        return HttpResponse('NGO Completed', content_type="application/text")
    else:
        feedback_form = UserFeedback_form()
        user_id = User.objects.get(username = request.session['username'])
        profile_data['name'] = user_id.first_name
        context = RequestContext(request)

        profile_data['is_upcomingrequests'] = True
        profile_data['is_ongoingrequests'] = True

        profile_data['upcoming_requests'] = list()
        profile_data['ongoing_requests'] = list()
        requests = list(Volunteer_ngo_request.objects.filter(recepient = user_id.id, status = "Accept"))
        for req in requests:
            if req.date_vol > datetime.date.today():
                profile_data['upcoming_requests'].append(req)
            elif req.date_vol == datetime.date.today() and req.time_vol > datetime.datetime.now().time():
                profile_data['upcoming_requests'].append(req)
            else:
                profile_data['ongoing_requests'].append(req)

        user_completed = list(Volunteer_ngo_request.objects.filter(recepient = user_id.id, status = "User Complete"))
        for req in user_completed:
            profile_data['ongoing_requests'].append(req)

        if len(profile_data['upcoming_requests']) == 0:
            profile_data['is_upcomingrequests'] = False

        if len(profile_data['ongoing_requests']) == 0:
            profile_data['is_ongoingrequests'] = False
        profile_data['is_ongoingrequests'] = False

        profile_data['is_pendingrequests'] = True
        profile_data['pending_requests'] = list(Volunteer_ngo_request.objects.filter(recepient = user_id.id, status = "Pending"))
        if len(profile_data['pending_requests']) == 0:
            profile_data['is_pendingrequests'] = False

        profile_data['is_pendingrecur'] = True
        profile_data['recurring_requests'] = list(Recurring_request.objects.filter(recepient = user_id.id, status = "Pending"))
        if len(profile_data['recurring_requests']) == 0:
            profile_data['is_pendingrecur'] = False
        return render_to_response('home/ngo/ngorequests.html', profile_data, context)

    #def match(a):
    #    if(a==""):
#        return Volunteer_ngo_request.objects.all
#    else:
#        return Volunteer_ngo_request.objects.filter(username=a)