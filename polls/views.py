from django.shortcuts import render,redirect, render_to_response
#from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
#from __future__ import unicode_literals
#from django.core.urlresolvers import reverse
#from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib.auth import authenticate
#from polls.models import student
from polls.models import course
from django.contrib.auth.models import User
# Create your views here.dfbdf
def home(request):
	print "I am here"
	
	return render(request,'home.html')
def signup(request):
	print "dddd"
    
	if request.method == 'POST':
		print "signup post"
		first_name = request.POST.get('username', None)
		username = request.POST.get('email',None)
		print username
		email = request.POST.get('email',None)
		print email
		password = request.POST.get('password',None)
		gender = request.POST.get('gender',None)
		intrest = request.POST.getlist('intrest',None)
		print intrest		
		intrest=[int(i) for i in intrest]
		print intrest
		#intr="intrest" in request.POST
		country = request.POST.get('country',None)
		user = User.objects.create_user(username,email,password)
		register = course(first_name=first_name,name=first_name, email=email, password=password, gender=gender, intrest=intrest,country=country)
		if username and email !='':
			print "save"
			if  email == course(email=email):
				print"duplicate"
				name_msg="Name is already taken"
				context={'name_msg1':name_msg1};
				return render(request,'signup.html',context)
			
			register.save()	
			user.first_name =first_name
			
			
			user.save()
			print "success"
			return redirect('/login/')
	else:
		#name_msg="please Register here"
		#context={'name_msg':name_msg};
			
		return render(request,'signup.html')
def login(request):
	if request.method == 'POST':
		#username=request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		#print username,password
		user = authenticate(username=email, password=password)
		print user
		if user:
			print "success"
			return redirect('/home/')
		else:
			print "bye"
			field="please check your credentials"
			context={'field':field};
			return  render(request,'login.html',context) 
	else:    
		return render(request,'login.html')

	 
	 