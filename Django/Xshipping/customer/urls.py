"""Xshipping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
	path('layout',views.layout, name='layout'),
	path('index/',views.index, name='index'),
    path('contact_us',views.contact_us, name='contact_us'),
    path('about_us/',views.about_us, name='about_us'),
    path('myform',views.myform, name='myform'),
    path('add_order1',views.add_order1, name='add_order1'),
    path('Senderorder/', views.Senderorder, name='Senderorder'),
    path('add_order2',views.add_order2, name='add_order2'),
    path('Receiverorder/',views.Receiverorder, name='Receiverorder'),
    path('add_order3', views.add_order3, name='add_order3'),
    path('Orderinfo/',views.Orderinfo, name='Orderinfo'),
    path('add_order4', views.add_order4, name='add_order4'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('orderdetail', views.orderdetail, name='orderdetail'),
    # path('select_company/', views.select_company, name='select_company'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('faq', views.faq, name='faq'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('registration', views.registration, name='registration'),
    path('feedback1/', views.feedback1, name='feedback1'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),
    path('storefeedback/', views.storefeedback, name='storefeedback'),
    path('inquiry1/', views.inquiry1, name='inquiry1'),
    path('storeinquiry/', views.storeinquiry, name='storeinquiry'),
    path('store/', views.store, name='store'),
    path('login/',views.login, name='login'),
    path('login_check/',views.login_check, name='login_check'),
    path('logout/',views.logout, name='logout'),



    # path('payment', views.payment, name='payment'),
    # path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    # path('admin/', admin.site.urls),
]


