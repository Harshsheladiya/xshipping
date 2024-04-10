from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from customer.models import profile,OrderInfo
from customer.models import feedback,inquiry,ReceiverOrder,SenderOrder
from myadmin.models import company_reg
from django.contrib import auth,messages
from django.conf import settings
import razorpay
import os
from django.contrib.auth.decorators import login_required
from .models import SenderOrder, ReceiverOrder, OrderInfo

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

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
        quantity = request.POST.get('quantity')
        unit_price = request.POST.get('unit_price')
        weight = request.POST.get('weight')
        length = request.POST.get('length')
        width = request.POST.get('width')
        height = request.POST.get('height')
        payment_method = request.POST.get('payment_method')
        total = request.POST.get('total')
        
        # Create and save the Order object
        Orderinfo = OrderInfo.objects.create(
            date=date,
            order_type=order_type,
            product_name=product_name,
            quantity=quantity,
            unit_price=unit_price,
            weight=weight,
            length=length,
            width=width,
            height=height,
            payment_method=payment_method,
            total=total,
            primary_user_id=request.user.id
        )

        return redirect('success_page')  
    
    return render(request, 'add_order3.html')

     


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





razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def payment(request):
    currency = 'INR'
    amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'customer/payment.html', context=context)

 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
