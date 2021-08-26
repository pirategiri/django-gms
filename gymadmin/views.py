from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.http import HttpResponse
from gyms.models import *
from .forms import GymForm

# def daCreate your views here.
def dashboard(request):
	context={}
	template = loader.get_template('dashboard.html')
	logged_in = False
	user = ''
	profile_complete = 0
	if is_authenticated(request):
		
		user = request.session.get('username')
		profile_complete = request.session.get('profile_complete')
		logged_in = True
		userObj = User.objects.filter(username=user).first()
		gymObj= Gym.objects.filter(user=userObj.pk)
		request.session['gym_count']=gymObj.count()

		context = {
			'logged_in': logged_in,
			'username':user,
			'profile_complete': profile_complete,
			'gym_count':gymObj.count(),
			'user':userObj,
			
			}
		request.session['gym_count']
		return HttpResponse(template.render(context, request))
	else:
		return redirect('/login')

def CreateGym(request):
	if is_authenticated(request):
		gym_count=request.session.get('gym_count')
		profile_complete = request.session.get('profile_complete')
		if request.POST:
			gym_form=GymForm(request.POST)
			if gym_form.is_valid():
				gym=gym_form.save()
				return redirect("/gymadmin/gyms/")
			else:
				gym_form=GymForm()
				template = loader.get_template('add_gym.html')
				context ={'gym_form':gym_form,'gym_count':gym_count,'logged_in':True}
				return HttpResponse(template.render(context, request))

		gym_form=GymForm()
		template = loader.get_template('add_gym.html')
		context ={'gym_form':gym_form,'gym_count':gym_count}
		return HttpResponse(template.render(context, request))
	else:
		return redirect('/login')

def gyms(request):
	if is_authenticated(request):
		
		template = loader.get_template('gyms/home.html')
		user_id=request.session.get('user_id')
		user = request.session.get('username')
		gym_count=request.session.get('gym_count')
		gyms=Gym.objects.filter(user_id=user_id)
		context ={'gyms':gyms,'gym_count':gym_count,'user':user,'logged_in':True}
		return HttpResponse(template.render(context, request)) 
		
	else:
		return redirect('/login')
def details(request,gym_id):
	if is_authenticated(request):
		template = loader.get_template('gyms/details.html')
		gym_count= request.session.get('gym_count')
		user = request.session.get('username')
		gym=Gym.objects.filter(pk=gym_id).first()
		userObj = User.objects.filter(username=user).first()
		if gym.user_id==userObj.id:
			context ={'gym':gym,'gym_count':gym_count,'user':user,'logged_in':True}
			return HttpResponse(template.render(context, request)) 
		else:
			return redirect('gymadmin/gyms/')
	else:
		return redirect('/login')
def delete(request,gym_id):
	if is_authenticated(request):
		#template = loader.get_template('gyms/details.html')
		#gym_count= request.session.get('gym_count')
		#user = request.session.get('username')
		gym=Gym.objects.filter(pk=gym_id).first()
		gym.delete()
		return redirect('/gymadmin/gyms')
		
		#context ={'gym':gym,'gym_count':gym_count,'user':user}
		return HttpResponse(template.render(context, request)) 
	else:
		return redirect('/login')

def edit(request,gym_id):
	if is_authenticated(request):
		gym_count= request.session.get('gym_count')
		gym_form=GymForm()
		if request.method=="POST":
			gym_form=GymForm(request.POST)
			gym_id=request.POST.get("gym_id")
			gym=Gym.objects.filter(pk=gym_id).first()
			if gym_form.is_valid():
				gym.name=gym_form.cleaned_data["name"]
				gym.location=gym_form.cleaned_data["location"]
				gym.price=gym_form.cleaned_data["price"]
				gym.summary=gym_form.cleaned_data["summary"]
				gym.featured_photos=gym_form.cleaned_data["featured_photos"]
				gym.user=gym_form.cleaned_data["user"]
				gym.save()
				return redirect("/gymadmin/gyms/")
		else:		
			gym=Gym.objects.filter(pk=gym_id).first()
			template = loader.get_template('gyms/edit_gym.html')
			user = request.session.get('username')
			
			context ={'gym_form':gym_form,'gym_count':gym_count,'gym':gym,'logged_in':True}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/login')



def is_authenticated(request):
	user=request.session.get('username')
	return user

