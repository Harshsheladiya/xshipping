from django.db import models
from django.contrib.auth.models import User

class price_reg(models.Model):
	user 			= 	models.ForeignKey(User, on_delete=models.CASCADE,default="")
	from_city		=	models.CharField(max_length=20)
	to_city 		= 	models.CharField(max_length=20)
	package_weight 	= 	models.CharField(max_length=20)
	price 			=	models.BigIntegerField()
	
	class Meta:
		db_table='add_price'