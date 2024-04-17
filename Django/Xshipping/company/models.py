from django.db import models
from django.contrib.auth.models import User
from myadmin.models import company_reg

class price_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    from_city = models.CharField(max_length=20)
    to_city = models.CharField(max_length=20)
    package_weight = models.CharField(max_length=20)
    price = models.BigIntegerField()
    # Define a ForeignKey to company_reg with a default value
    company = models.ForeignKey(company_reg, on_delete=models.CASCADE, default=1)
    
    class Meta:
        db_table = 'add_price'
