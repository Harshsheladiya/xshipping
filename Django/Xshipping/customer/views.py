from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from customer.models import profile,OrderInfo
from customer.models import feedback,inquiry,ReceiverOrder,SenderOrder
from myadmin.models import company_reg
from company.models import price_reg
from django.contrib import auth,messages
from django.conf import settings
import razorpay
import os
from django.contrib.auth.decorators import login_required
from .models import SenderOrder, ReceiverOrder, OrderInfo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from decimal import Decimal
from itertools import zip_longest


def layout(request):
	return render(request,'customer/common/layout.html')

# def index(request):
# 	context={}
# 	return render(request,'customer/index.html',context)

def contact_us(request):
	context={}
	return render(request,'customer/contact_us.html',context)

def about_us(request):
	context={}
	return render(request,'customer/about_us.html',context)

def myform(request):
	context={}
	return render(request,'customer/form.html',context)

def myprofile(request):
	id=request.user.id
	result1=profile.objects.get(user_id=id)
	context={'result1':result1}
	return render(request,'customer/profile.html',context)

def add_order1(request):
	context={}
	return render(request,'customer/add_order1.html',context)

def add_order2(request):
	context={}
	return render(request,'customer/add_order2.html',context)

def add_order3(request):
	context={}
	return render(request,'customer/add_order3.html',context)
	
def add_order4(request):
	context={}
	return render(request,'customer/add_order4.html',context)

def faq(request):
	context={}
	return render(request,'customer/faq.html',context)

def portfolio(request):
	context={}
	return render(request,'customer/portfolio.html',context)

def registration(request):
	context={}
	return render(request,'customer/customer_register.html',context)

def feedback1(request):
	context={}
	return render(request,'customer/feedback1.html',context)

def storefeedback(request):
	name   		= request.POST['fname']
	email 		= request.POST['email']
	contact 	= request.POST['contact']
	message 	= request.POST['message']
	
	feedback.objects.create(name=name,contact=contact,email=email,message=message,user_id=request.user.id)
	return redirect('/customer/feedback1/')

def inquiry1(request):
	result=company_reg.objects.all()
	context={'result':result}
	return render(request,'customer/inquiry1.html',context)

def storeinquiry(request):
	name   		= request.POST['fname']
	email 		= request.POST['email']
	contact 	= request.POST['contact']
	subject 	= request.POST['subject']
	message 	= request.POST['message']
	company 	= request.POST['company']
	inquiry.objects.create(name=name,contact=contact,email=email,subject=subject,message=message,primary_user_id=request.user.id,secondary_user_id=company)
	return redirect('/customer/inquiry1/')



# -------------------------------------------login--------------------------

def login(request):
	context={}
	return render(request,'customer/login.html',context)

def index(request):
	id=request.user.id
	result= User.objects.get(pk=id)
	result1=profile.objects.get(user_id=id)
	context={'result':result,'result1':result1}
	return render(request,'customer/index.html',context)

def login_check(request):
	username=request.POST['username']
	password=request.POST['password']

	result = auth.authenticate(username=username,password=password)

	if result is None:
		messages.error(request,'username or password are invalid')
		return redirect('/customer/login/')
	else:
		auth.login(request,result)
		return redirect('/customer/index/')

def logout(request):
	auth.logout(request)
	return redirect('/customer/login/')

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .models import profile  # Assuming you have a Profile model defined

def store(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        city = request.POST.get('city')

        if not (user_name and fname and email and password and cpassword and contact and gender and address and pincode and state and city):
            # Handle case where required fields are missing
            messages.error(request, 'All fields are required.')
            return redirect('/customer/registration/')
        
        if password == cpassword:
            # Create user
            user = User.objects.create_user(username=user_name, first_name=fname, email=email, password=password)
            # Set additional user attributes
            user.first_name = fname
            user.phone = contact
            user.save()

            # Create profile
            profile = Profile.objects.create(contact=contact, gender=gender, address=address, pincode=pincode, state=state, city=city, user_id=user.id)

            # Redirect to login page
            return redirect('/customer/login/')
        else:
            messages.error(request, 'Password and confirm password do not match.')
            return redirect('/customer/registration/')
    else:
        # Handle case where request method is not POST
        messages.error(request, 'Invalid request method.')
        return redirect('/customer/registration/')


		
def orderdetail(request):
	context={}
	return render(request,'customer/orderdetail.html',context)

def viewfeedback(request):
	context={}
	return render(request,'customer/viewfeedback.html',context)




def inquiry1(request):
	result=company_reg.objects.all()
	context={'result':result}
	return render(request,'customer/inquiry1.html',context)


def Senderorder(request):
    if request.method == 'POST':
        # Retrieve form data
        Sender_name = request.POST.get('Sender_name')
        Sender_email = request.POST.get('Sender_email')
        Sender_phone_number = request.POST.get('Sender_phone_number')
        Sender_alternate_phone_number = request.POST.get('Sender_alternate_phone_number')
        Pickup_address_line1 = request.POST.get('Pickup_address_line1')
        Pickup_address_line2 = request.POST.get('Pickup_address_line2')
        Sender_pincode = request.POST.get('Sender_pincode')
        Sender_city = request.POST.get('Sender_city')
        Sender_state = request.POST.get('Sender_state')
        Sender_country = request.POST.get('Sender_country')
		
		
        
        # Create and save order object
        Senderorder = SenderOrder(
            Sender_name=Sender_name,
            Sender_email=Sender_email,
            Sender_phone_number=Sender_phone_number,
            Sender_alternate_phone_number=Sender_alternate_phone_number,
            Pickup_address_line1=Pickup_address_line1,
            Pickup_address_line2=Pickup_address_line2,
            Sender_pincode=Sender_pincode,
            Sender_city=Sender_city,
            Sender_state=Sender_state,
            Sender_country=Sender_country,
			primary_user_id=request.user.id     
 		)


        Senderorder.save()

        # Redirect to the next page or render a success message
        return redirect('add_order2')  # Replace 'add_order2.html' with the URL of the next page
    else:
        return render(request, 'add_order1.html')


def Receiverorder(request):
    if request.method == 'POST':
        # Retrieve form data
        Receiver_name = request.POST.get('Receiver_name')
        Receiver_email = request.POST.get('Receiver_email')
        Receiver_phone_number = request.POST.get('Receiver_phone_number')
        Receiver_alternate_phone_number = request.POST.get('Receiver_alternate_phone_number')
        Delivery_address_line1 = request.POST.get('Delivery_address_line1')
        Delivery_address_line2 = request.POST.get('Delivery_address_line2')
        Receiver_pincode = request.POST.get('Receiver_pincode')
        Receiver_city = request.POST.get('Receiver_city')
        Receiver_state = request.POST.get('Receiver_state')
        Receiver_country = request.POST.get('Receiver_country')
		
		
        
        # Create and save order object
        Receiverorder = ReceiverOrder(
            Receiver_name=Receiver_name,
            Receiver_email=Receiver_email,
            Receiver_phone_number=Receiver_phone_number,
            Receiver_alternate_phone_number=Receiver_alternate_phone_number,
            Delivery_address_line1=Delivery_address_line1,
            Delivery_address_line2=Delivery_address_line2,
            Receiver_pincode=Receiver_pincode,
            Receiver_city=Receiver_city,
            Receiver_state=Receiver_state,
            Receiver_country=Receiver_country,
			primary_user_id=request.user.id   
        )
        Receiverorder.save()

        # Redirect to the next page or render a success message
        return redirect('add_order3')  # Replace 'add_order2.html' with the URL of the next page
    else:
        return render(request, 'add_order2.html')

	


def Orderinfo(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        order_type = request.POST.get('order_type')
        product_name = request.POST.get('product_name')
        # quantity = request.POST.get('quantity')
        # unit_price = request.POST.get('unit_price')
        weight = request.POST.get('weight')
        length = request.POST.get('length')
        width = request.POST.get('width')
        height = request.POST.get('height')
        payment_method = request.POST.get('payment_method')
        # total = request.POST.get('total')
        
        # Create and save the Order object
        Orderinfo = OrderInfo.objects.create(
            date=date,
            order_type=order_type,
            product_name=product_name,
            # quantity=quantity,
            # unit_price=unit_price,
            weight=weight,
            length=length,
            width=width,
            height=height,
            payment_method=payment_method,
            # total=total,
            primary_user_id=request.user.id
        )
    
        return redirect('order_summary')  
    
    return render(request, 'customer/add_order3.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import SenderOrder, ReceiverOrder, OrderInfo
from django.db.models import Q

@login_required
def order_summary(request):
    # Retrieve distinct sender and receiver information
    sender_order = SenderOrder.objects.filter(primary_user=request.user).order_by('-id').first()
    receiver_order = ReceiverOrder.objects.filter(primary_user=request.user).order_by('-id').first()

    # Check if sender_order and receiver_order are None
    if sender_order is None or receiver_order is None:
        # Handle the case where sender_order or receiver_order is not found
        return render(request, 'error_template.html', {'error_message': 'Sender order or receiver order not found'})

    sender_city = sender_order.Sender_city 
    receiver_city = receiver_order.Receiver_city 

    # Retrieve distinct package weights from the price_reg model
    package_weights_decimal = price_reg.objects.values_list('package_weight', flat=True).distinct()
    # Convert Decimal objects to string for display
    package_weights = [str(weight) for weight in package_weights_decimal]

    # Retrieve the latest OrderInfo for the user
    latest_order_info = OrderInfo.objects.filter(primary_user=request.user).order_by('-id').first()

    # Mapping predefined weights to their corresponding ranges
    weight_ranges = {
        '0-20': '5-20kg',
        '21-50': '21-50kg',
        '51-100': '51-100kg',
    }

    # Get the weight range based on the weight
    weight_display = None
    if latest_order_info is not None:
        weight = Decimal(str(latest_order_info.weight))  # Convert Decimal to string
        for range_key, range_value in weight_ranges.items():
            start, end = map(int, range_key.split('-'))
            if start <= weight <= end:
                weight_display = range_value
                break
        if weight_display is None:
            weight_display = str(weight) + 'kg'  # If weight is not within predefined ranges, display the original weight

    # Retrieve company information based on weight ranges
    weight_company_map = {}
    weight_company_mapp = {}

    for weight_range in package_weights:
        companiess = company_reg.objects.filter(price_reg__from_city=sender_city, price_reg__to_city=receiver_city, price_reg__package_weight=weight_range).distinct()
        weight_company_mapp[weight_range] = companiess

    # Ensure that companies_map and companiess are of the same length
    for weight_range, companies in weight_company_mapp.items():
        companies_map = price_reg.objects.filter(from_city=sender_city, to_city=receiver_city, package_weight=weight_range).distinct()
        zipped_data = zip_longest(companies, companies_map)
        weight_company_map[weight_range] = zipped_data

    context = {
        'sender_order': sender_order,
        'receiver_order': receiver_order,
        'sender_city': sender_city,  # Add sender_city to context
        'receiver_city': receiver_city,  # Add receiver_city to context
        'latest_order_info': latest_order_info,
        'package_weights': package_weights,
        'weight_display': weight_display,
        'weight_company_map': weight_company_map,
        'weight_company_mapp': weight_company_mapp,
    }

    return render(request, 'customer/order_summary.html', context)



@login_required
def orderdetail(request):
    sender_orders = SenderOrder.objects.filter(primary_user=request.user)
    receiver_orders = ReceiverOrder.objects.filter(primary_user=request.user)
    order_infos = OrderInfo.objects.filter(primary_user=request.user)

    context = {
        'sender_orders': sender_orders,
        'receiver_orders': receiver_orders,
        'order_infos': order_infos,
        'company_name': request.user.first_name  # Assuming you have company name in the user profile
    }
    return render(request, 'customer/orderdetail.html', context)





import razorpay
from django.conf import settings
from django.http import JsonResponse
import time 
from razorpay import Client

def process_payment(request):
    if request.method == 'POST':
        total_amount = request.POST.get('total')
        total_amount_in_paisa = int(float(total_amount)*100 )
        
        client = Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment_data = {
            'amount': total_amount_in_paisa,
            'currency': 'INR',
            'receipt': 'order_receipt_' + str(int(time.time())),  # Unique order receipt
        }
        payment = client.order.create(data=payment_data)
        
        context = {
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'amount': total_amount_in_paisa,
            'order_id': payment['id'],
            'user_name': request.user.first_name,  # Replace with your user's name field
            'user_email': request.user.email,  # Replace with your user's email field
            # 'user_phone': request.user.Contact,  # Replace with your user's phone field
            # 'user_address': request.user.address,  # Replace with your user's address field
        }
        return render(request, 'customer/payment.html', context)


def payment_success(request):
    return render(request, 'customer/payment_success.html')