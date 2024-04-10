from django.db import models
from django.contrib.auth.models import User
from myadmin.models import company_reg
from django.db import models

class profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
	contact=models.BigIntegerField()
	gender=models.CharField(max_length=10)
	address=models.TextField()
	pincode=models.BigIntegerField()
	state=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	
	class Meta:
		db_table='profile'


class feedback(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.CharField(max_length=20)
	email=models.EmailField()
	contact=models.BigIntegerField()
	message=models.TextField()
	
	class Meta:
		db_table='feedback'

class inquiry(models.Model):
	primary_user = models.ForeignKey(User,on_delete=models.CASCADE,default="",related_name='customer')
	secondary_user = models.ForeignKey(User,on_delete=models.CASCADE,default="",related_name='company')
	name=models.CharField(max_length=20)
	email=models.EmailField()			
	contact=models.BigIntegerField()
	subject=models.CharField(max_length=50)
	message=models.TextField()
	
	class Meta:
		db_table='inquiry'


class SenderOrder(models.Model):
    primary_user = models.ForeignKey(User, on_delete=models.CASCADE,default="" ,related_name='sender_orders')
    # secondary_user = models.ForeignKey(User,on_delete=models.CASCADE,default="",related_name='company')
    Sender_name = models.CharField(max_length=100)
    Sender_email = models.EmailField()
    Sender_phone_number = models.CharField(max_length=15)
    Sender_alternate_phone_number = models.CharField(max_length=15, blank=True, null=True)
    Pickup_address_line1 = models.CharField(max_length=255)
    Pickup_address_line2 = models.CharField(max_length=255)
    Sender_pincode = models.CharField(max_length=6)
    Sender_city = models.CharField(max_length=100)
    Sender_state = models.CharField(max_length=100)
    Sender_country = models.CharField(max_length=100)
	

    # Add any additional fields as needed

    def __str__(self):
        return self.Sender_name  # or any other field you want to display as the object representation


    class Meta:
        db_table = 'Senderorder'



class ReceiverOrder(models.Model):
    primary_user = models.ForeignKey(User, on_delete=models.CASCADE,default="", related_name='receiver_orders')
    # secondary_user = models.ForeignKey(User,on_delete=models.CASCADE,default="",related_name='company')
    Receiver_name = models.CharField(max_length=100)
    Receiver_email = models.EmailField()
    Receiver_phone_number = models.CharField(max_length=15)
    Receiver_alternate_phone_number = models.CharField(max_length=15, blank=True, null=True)
    Delivery_address_line1 = models.CharField(max_length=255)
    Delivery_address_line2 = models.CharField(max_length=255)
    Receiver_pincode = models.CharField(max_length=6)
    Receiver_city = models.CharField(max_length=100)
    Receiver_state = models.CharField(max_length=100)
    Receiver_country = models.CharField(max_length=100)
	

    # Add any additional fields as needed

    def __str__(self):
        return self.Receiver_name  # or any other field you want to display as the object representation


    class Meta:
        db_table = 'Receiverorder'





class OrderInfo(models.Model):
    primary_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_infos')
    date = models.DateField()
    order_type = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)  
    length = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) 
    width = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)   
    height = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Default value added here
    payment_method = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Orderinfo'


