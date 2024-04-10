from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from myadmin.models import company_reg
from company.models import price_reg
from customer.models import profile,feedback,inquiry

# Create your views here.

# def dashboard(request):
# 	context={}
# 	return render(request,'company/dashboard.html',context)

def order_list(request):
	context={}
	return render(request,'company/order_list.html',context)

def register(request):
	context={}
	return render(request,'company/register.html',context)

def feedback1(request):
	context={}
	return render(request,'company/feedback.html',context)

def readfeedback(request):
	readf= feedback.objects.all()
	context={'readf': readf}
	return render(request,'company/feedback.html',context)

def feedbackform(request):
	context={}
	return render(request,'company/feedbackform.html',context)

def inquiryform(request):
	context={}
	return render(request,'company/inquiryform.html',context)

def inquiry1(request):
	context={}
	return render(request,'company/inquiry.html',context)

def readinquiry(request):
	id=request.user.id
	readf=inquiry.objects.filter(secondary_user_id=id)
	context={'readf': readf}
	return render(request,'company/inquiry.html',context)

def res_inquiries(request):
	context={}
	return render(request,'company/res_inquiries.html',context)

def reports(request):
	context={}
	return render(request,'company/reports.html',context)

def res_reports(request):
	context={}
	return render(request,'company/res_reports.html',context)

def reportform(request):
	context={}
	return render(request,'company/reportform.html',context)

def add_price(request):
	context={}
	return render(request,'company/Add_price.html',context)

def view_price(request):
	context={}
	return render(request,'company/view_price.html',context)

def viewprice(request):
	id=request.user.id
	readf=price_reg.objects.filter(user_id=id)
	context={'readf': readf}
	return render(request,'company/view_price.html',context)

def store_price(request):
	from_city   = request.POST['fromcity']
	to_city 	= request.POST['tocity']
	weight      = request.POST['weight']
	price 		= request.POST['price']

	price_reg.objects.create(from_city=from_city,to_city=to_city,package_weight=weight,price=price,user_id=request.user.id)
	return redirect('/company/add_price/')


def customer_profile(request):
	context={}
	return render(request,'company/customer_profile.html',context)

def my_profile(request):
	id=request.user.id
	result= User.objects.get(pk=id)
	result1=company_reg.objects.get(user_id=id)
	context={'result':result,'result1':result1}
	return render(request,'company/my_profile.html',context)

def login(request):
	context={}
	return render(request,'company/login.html',context)

def dashboard(request):
	id=request.user.id
	result= User.objects.get(pk=id)
	result1=company_reg.objects.get(user_id=id)
	context={'result':result,'result1':result1}
	return render(request,'company/dashboard.html',context)

def login_check(request):
	username=request.POST['username']
	password=request.POST['password']

	result = auth.authenticate(username=username,password=password)

	if result is None:
		print('Invalid username or password')
		return redirect('/company/login/')
	else:
		auth.login(request,result)
		return redirect('/company/dashboard/')

def logout(request):
	auth.logout(request)
	return redirect('/company/login/')

def update_profile(request):
	id=request.user.id
	readf= User.objects.get(pk=id)
	readg=company_reg.objects.get(user_id=id)
	context={'readf':readf,'readg':readg}
	return render(request,'company/update_profile.html',context)

def update(request,id):
	user_name   = request.POST['username']
	fname 		= request.POST['fname']
	email 		= request.POST['email']
	Myfile 		= request.FILES['myfile']

	mylocation	= os.path.join(settings.MEDIA_ROOT,'upload')
	obj=FileSystemStorage(location=mylocation)
	obj.save(Myfile.name,Myfile)

	owner_name  = request.POST['owner_name']
	contact     = request.POST['contact']
	address     = request.POST['address']

	User.objects.update_or_create(pk=id,defaults={'username':user_name,'first_name':fname,'email':email})
	company_reg.objects.update_or_create(user_id=id,defaults={'owner_name':owner_name,'contact':contact,'address':address,'filename':Myfile})
	
	return redirect('/company/my_profile/')

#____________________delete company_____________
def destroy(request):
	id=request.user.id
	readf= User.objects.get(pk=id)
	readg=company_reg.objects.get(user_id=id)
	readf.delete()
	readg.delete()
	return redirect('/company/login/')