from django.contrib import admin

# Register your models here.
from . models import inquiry
from . models import profile
from . models import feedback
from . models import ReceiverOrder
from . models import SenderOrder
from . models import OrderInfo
# from . models import CompanyOrder

admin.site.register(inquiry)
admin.site.register(profile)
admin.site.register(feedback)
admin.site.register(ReceiverOrder)
admin.site.register(SenderOrder)
admin.site.register(OrderInfo)
# admin.site.register(CompanyOrder)
