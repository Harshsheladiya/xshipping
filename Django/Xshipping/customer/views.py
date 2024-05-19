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
	#auth user
	user_name   = request.POST['username']
	fname 		= request.POST['fname']
	email 		= request.POST['email']
	password 	= request.POST['password']
	cpassword 	= request.POST['cpassword']
	contact 	= request.POST['contact']
	gender 		= request.POST['gender']
	address 	= request.POST['address']
	pincode 	= request.POST['pincode']
	state 		= request.POST['state']
	city 		= request.POST['city']
	
	


	if password==cpassword:
		user = User.objects.create_user(username=user_name,first_name=fname,email=email,password=password)

		profile.objects.create(contact=contact,gender=gender,address=address,pincode=pincode,state=state,city=city,user_id=user.id)
		return redirect('/customer/login/')
	else:
		messages.error(request,'password and confirm password is mismatched')
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

def order_summary(request):
    sender_order = SenderOrder.objects.filter(primary_user=request.user).order_by('-id').first()
    receiver_order = ReceiverOrder.objects.filter(primary_user=request.user).order_by('-id').first()

    if sender_order is None or receiver_order is None:
        return render(request, 'error_template.html', {'error_message': 'Sender order or receiver order not found'})

    sender_city = sender_order.Sender_city
    receiver_city = receiver_order.Receiver_city

    package_weights_decimal = price_reg.objects.values_list('package_weight', flat=True).distinct()
    package_weights = [str(weight) for weight in package_weights_decimal]

    latest_order_info = OrderInfo.objects.filter(primary_user=request.user).order_by('-id').first()

    weight_ranges = {
        '0-20': '5-20kg',
        '21-50': '21-50kg',
        '51-100': '51-100kg',
    }

    weight_display = None
    if latest_order_info is not None:
        weight = Decimal(str(latest_order_info.weight))
        for range_key, range_value in weight_ranges.items():
            start, end = map(int, range_key.split('-'))
            if start <= weight <= end:
                weight_display = range_value
                break
        if weight_display is None:
            weight_display = str(weight) + 'kg'

    weight_company_map = {}
    weight_company_mapp = {}

    for weight_range in package_weights:
        companiess = company_reg.objects.filter(price_reg__from_city=sender_city, price_reg__to_city=receiver_city, price_reg__package_weight=weight_range).distinct()
        weight_company_mapp[weight_range] = companiess

    for weight_range, companies in weight_company_mapp.items():
        companies_map = price_reg.objects.filter(from_city=sender_city, to_city=receiver_city, package_weight=weight_range).distinct()
        zipped_data = zip_longest(companies, companies_map)
        weight_company_map[weight_range] = zipped_data
        fname = request.user.first_name 
    context = {
        'sender_order': sender_order,
        'receiver_order': receiver_order,
        'sender_city': sender_city,
        'receiver_city': receiver_city,
        'latest_order_info': latest_order_info,
        'package_weights': package_weights,
        'weight_display': weight_display,
        'weight_company_map': weight_company_map,
        'weight_company_mapp': weight_company_mapp,
        'fname': fname,
        
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
# from twilio.rest import Client as TwilioClient  # Rename to avoid conflict with Razorpay Client
from django.shortcuts import render

def process_payment(request):
    if request.method == 'POST':
        try:
            total_amount = request.POST.get('total')
            total_amount_in_paisa = int(float(total_amount) * 100)

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
                'user_phone': request.user.profile.contact,  # Update to access contact field from the profile
                'user_address': request.user.profile.address,  # Replace with your user's address field
            }
            return render(request, 'customer/payment.html', context)
        except Exception as e:
            # Handle any errors that occur during payment processing
            return JsonResponse({'success': False, 'message': str(e)})

def send_sms(to, body):
    try:
        client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to
        )
        # Log the SID of the sent message for reference
        print("Message SID:", message.sid)
        return message.sid
    except Exception as e:
        # Handle any errors that occur during SMS sending
        print("Error sending SMS:", e)
        return None


def payment_success(request):
    try:
        # Your payment success logic here
        # Example: sending an SMS
        total_amount = request.POST.get('total')
        payment_id = request.POST.get('payment_id')
        user_phone_number = request.user.profile.contact  # Assuming this is how you get the user's phone number
        message_body = f"Payment successful! Amount: {total_amount} Payment ID: {payment_id}"
        send_sms(user_phone_number, message_body)
        return render(request, 'customer/payment_success.html')
    except Exception as e:
        # Handle any errors that occur during SMS sending
        return JsonResponse({'success': False, 'message': str(e)})
 


def viewfeedback(request):
    readf= feedback.objects.all()
    context={'readf': readf}
    return render(request, 'customer/viewfeedback.html', context)
