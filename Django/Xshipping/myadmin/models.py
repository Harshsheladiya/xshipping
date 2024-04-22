from django.db import models
from django.contrib.auth.models import User

class company_reg(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
	owner_name=models.CharField(max_length=30)
	filename = models.CharField(max_length=255)
	contact=models.BigIntegerField()
	address=models.TextField()

	class Meta:
		db_table='companies'

