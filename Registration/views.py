from django.shortcuts import render, render_to_response
from Registration.forms import UserForm, UserProfileForm, NGOProfileForm, NGOEmployeeProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from Registration.models import User, UserProfile, NGOProfile, NGOEmployeeProfile, NGODomains
from Requests.models import Activity
from Home.tasks import duplicate
def user_register(request):
    registered = False
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            #save user data to database
            user = user_form.save()
            #hashing password to allow us to edit the user object
            user.set_password(user.password)
            user.save()
            #User Profile Instance

            luser = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))

            if luser:
                login(request, luser)
                request.session['username'] = request.POST.get('username')
            else:
                return HttpResponse (request.POST.get('username'), request.POST.get('password'))
            return HttpResponseRedirect('/register/profile/')
        else:
            print user_form.errors
    else:
        user_form = UserForm()
        return render_to_response('registration/ind_reg.html',{'user_form':user_form}, context)

def ngo_register(request):
    #boolean value for telling the template whether thr registration was successful
    #initially set to false
    registered = False
    context = RequestContext(request)
    if request.method == 'POST': #for processing the form data
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            #save user data to database
            user = user_form.save()
            #hashing password to allow us to edit the user pbjecto
            user.set_password(user.password)
            user.save()
            #User Profile Instance
            luser = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))

            if luser:
                login(request, luser)
                request.session['username'] = request.POST.get('username')
            else:
                return HttpResponse (request.POST.get('username'), request.POST.get('password'))

            try:
                NGOEmployeeProfile.objects.get(user_id=user.id)
            except:
                employee=NGOEmployeeProfile.objects.create(position="Owner",admin=True,user_id=user.id)
                registered = True
            return HttpResponseRedirect('/register/ngoprofile/')

        else:
            print user_form.errors,
    else:
        #set forms blank if there is no HTTP POST
        user_form = UserForm()
        #render template depending on context
    return render_to_response('registration/ngo_reg.html',{'user_form': user_form, 'registered': registered}, context)

def user_ngo_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        #gather information from the login form
        username = request.POST.get('username')
        password = request.POST.get('password')
        #inbuilt django authentication
        user = authenticate(username = username, password = password)
        if user:
             login(request, user)
             request.session['username'] = username
             return HttpResponse('/')
        else:
            print "Invalid login details: {0} {1}".format(username, password)
            return HttpResponse("incorrect")
    else:
        return render_to_response('registration/login.html', {}, context)

@login_required
def user__ngo_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def update_profile(request):
    context = RequestContext(request)
    if request.method == 'POST':
        try:
            UserProfile.objects.get(user_id=request.user)
        except:
            p = UserProfile.objects.create(user_id=request.user.id, address=request.POST.get('address'), skill_math=request.POST.get('math'),skill_english=request.POST.get('english'),skill_science=request.POST.get('science'),skill_ict=request.POST.get('ict'),skill_socialmediamarket=request.POST.get('marketing'),skill_sport=request.POST.get('sport'),skill_programming=request.POST.get('programming'))
            for a in request.POST.getlist("interests"):
                p.interests.add(NGODomains.objects.get(domain=a))
            return HttpResponseRedirect("/")
    else:
        array=list(NGODomains.objects.filter())

        return render_to_response('registration/details.html', {'array':array}, context)

@login_required
def update_ngoprofile(request):
    context = RequestContext(request)
    if request.method == 'POST':

        profile_form = NGOProfileForm(data=request.POST)
        if profile_form.is_valid():
            try:
                NGOProfile.objects.get(ngo_id=request.user.id)
                return HttpResponse("Already exists")
            except:
                profile = profile_form.save(commit=False)
                profile.ngo_id = request.user.id
                profile.ngo_domain=NGODomains.objects.get(domain=request.POST.get('ngo_domain')).id
                x=NGOEmployeeProfile.objects.get(user_id=request.user.id)
                profile.save()
                x.ngo_id=profile.id

                for a in request.POST.getlist("activityname"):
                    profile.activity.add(Activity.objects.get(activityname=a))
                x.save()
                return HttpResponseRedirect("/")
        else:
            return HttpResponse("Invalid form")
    else:
        try:
            NGOProfile.objects.get(ngo_id=request.user.id)

        except:
            profile_form = NGOProfileForm()
            array=list(NGODomains.objects.filter())
            arrayact=list(Activity.objects.filter())
            return render_to_response('registration/ngo.html', {'profile_form':profile_form,'array':array,'arrayact':arrayact}, context)
    	return HttpResponseRedirect("/")

