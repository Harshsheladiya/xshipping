from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from myadmin.models import company_reg
from company.models import price_reg
from customer.models import inquiry,feedback,profile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your viewsmyadmin

def login(request):
	context={}
	return render(request,'myadmin/login.html',context)

def dashboard(request):
	id=request.user.id
	result= User.objects.get(pk=id)
	context={'result':result}
	return render(request,'myadmin/dashboard.html',context)

def login_check(request):
	username=request.POST['username']
	password=request.POST['password']

	result = auth.authenticate(username=username,password=password)

	if result is None:
		print('Invalid username or password')
		return redirect('/myadmin/login/')
	else:
		auth.login(request,result)
		return redirect('/myadmin/dashboard/')

def logout(request):
	auth.logout(request)
	return redirect('/myadmin/login/')

# def dashboard(request):
# 	context={}
# 	return render(request,'myadmin/dashboard.html',context)

def order_list(request):
	context={}
	return render(request,'myadmin/order_list.html',context)

def view_price(request):
	context={}
	return render(request,'myadmin/view_price.html',context)

def viewprice(request):
	readf= price_reg.objects.all()
	context={'readf': readf}
	return render(request,'myadmin/view_price.html',context)

def login(request):
	context={}
	return render(request,'myadmin/login.html',context)

def register(request):
	context={}
	return render(request,'myadmin/register.html',context)

def logistic_companies(request):
	context={}
	return render(request,'myadmin/logistic_companies.html',context)

def company_register(request):
	context={}
	return render(request,'myadmin/company_register.html',context)

def feedback1(request):
	context={}
	return render(request,'myadmin/feedback.html',context)

def readfeedback(request):
	readf= feedback.objects.all()
	context={'readf': readf}
	return render(request,'myadmin/feedback.html',context)

def inquiry1(request):
	context={}
	return render(request,'myadmin/inquiry.html',context)

def readinquiry(request):
	readf= inquiry.objects.all()
	context={'readf': readf}
	return render(request,'myadmin/inquiry.html',context)

def reports(request):
	context={}
	return render(request,'myadmin/reports.html',context)

def res_reports(request):
	context={}
	return render(request,'myadmin/res_reports.html',context)

def customer_profile(request):
	context={}
	return render(request,'myadmin/customer_profile.html',context)

def readcustomer(request):
	readf = profile.objects.all()
	context={'readf': readf}
	return render(request,'myadmin/customer_profile.html',context)

# store company_reg data
def store(request):
	#auth user
	user_name    = request.POST['username']
	fname 		= request.POST['fname']
	email 		= request.POST['email']
	password 	= request.POST['password']
	cpassword 	= request.POST['cpassword']
	#companies
	Myfile 		= request.FILES['myfile']
	mylocation	=os.path.join(settings.MEDIA_ROOT,'upload')
	obj=FileSystemStorage(location=mylocation)
	obj.save(Myfile.name,Myfile)

	owner_name 	= request.POST['owner_name']
	contact 	= request.POST['contact']
	address 	= request.POST['address']

	if password==cpassword:
		user = User.objects.create_user(username=user_name,first_name=fname,email=email,password=password)

		company_reg.objects.create(owner_name=owner_name,filename=Myfile,contact=contact,address=address,user_id=user.id)
	else:
		print('password and confirm password is mismatched')
	
	return redirect('/myadmin/company_register/')



#________________read companies_________________
def read(request):
    readf = company_reg.objects.all()
    # Fetch related data using reverse relation
    readg = User.objects.all()
    # Fetch related data from price_reg
    readh = price_reg.objects.select_related('user').all()
    context = {'readf': readf, 'readg': readg, 'readh': readh}
    return render(request, 'myadmin/logistic_companies.html', context)





def dashboard(request):
    profiles = profile.objects.all()  # Get all profiles
    companie = company_reg.objects.all()  # Get all companies
    
    context = {
        'profiles': profiles,
        'companie': companie,
    }
    
    return render(request, 'myadmin/dashboard.html', context)
