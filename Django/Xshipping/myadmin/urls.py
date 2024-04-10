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
from myadmin import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('order_list',views.order_list, name='order_list'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    #path('logistic_companies',views.logistic_companies, name='logistic_companies'),
    path('company_register/',views.company_register, name='company_register'),
    path('feedback1',views.readfeedback, name='readfeedback'),
    path('inquiry1',views.readinquiry, name='readinquiry'),
    #path('res_inquiries',views.res_inquiries, name='res_inquiries'),
    path('view_price',views.viewprice, name='viewprice'),
    path('reports',views.reports, name='reports'),
    path('res_reports',views.res_reports, name='res_reports'),
    path('customer_profile',views.readcustomer, name='readcustomer'),
    path('store/', views.store, name='store'), 
    path('logistic_companies/', views.read, name='read'),
    path('login/',views.login, name='login'),
    path('login_check/',views.login_check, name='login_check'),
    path('logout/',views.logout, name='logout'),
    
]
