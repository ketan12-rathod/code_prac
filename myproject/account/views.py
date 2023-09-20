from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import Profile, Feedback
from django.contrib import messages, auth

def register(request):
	context = {}
	return render(request,'account/register.html',context)

def register_store(request):
	myfname     = request.POST['fname']
	mylname     = request.POST['lname']
	myemail     = request.POST['email']
	myusername  = request.POST['username']
	mypassword  = request.POST['password']
	mycpassword = request.POST['cpassword']

	mycontact = request.POST['contact']
	myaddress = request.POST['address']

	if mypassword == mycpassword:
		user = User.objects.create_user(first_name=myfname,last_name=mylname,email=myemail,username=myusername,password=mypassword)
		Profile.objects.create(contact=mycontact,address=myaddress,user_id=user.id)
		messages.info(request, "You have registered successfully..")
		return redirect('/account/register')

	else:
		messages.info(request, "Missmatch Password")
		return redirect('/account/register')


def home(request):
	id = request.user.id
	profile = Profile.objects.get(user_id=id)
	context = {'profile':profile}
	return render(request,'account/index.html',context)

def login(request):
	context = {}
	return render(request,'account/login.html',context)

def login_check(request):
	myusername = request.POST['username']
	mypassword = request.POST['password']

	result = auth.authenticate(request, username=myusername, password=mypassword)

	if result is None:
		messages.info(request, 'Invalid Username or Password')
		return redirect('/account/login')
	else:
		auth.login(request, result)
		return redirect('/account/home')

def logout(request):
	auth.logout(request)
	return redirect('/account/login')


def feedback(request):
	context = {}
	return render(request,'account/feedback.html',context)

def feedback_store(request):
	myrating = request.POST['rating']
	mycomment = request.POST['comment']

	id = request.user.id
	Feedback.objects.create(rating=myrating,comment=mycomment,user_id=id)
	messages.info(request,'Feedback Sent Successfully')
	return redirect('/account/feedback')






















