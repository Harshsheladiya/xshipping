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
from company import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('order_list',views.order_list, name='order_list'),
    path('register',views.register, name='register'),
    path('feedback1',views.readfeedback, name='readfeedback'),
    path('feedbackform',views.feedbackform, name='feedbackform'),
    path('inquiryform',views.inquiryform, name='inquiryform'),
    path('inquiry1',views.readinquiry, name='readinquiry'),
    # path('res_inquiries',views.res_inquiries, name='res_inquiries'),
    path('reportform',views.reportform, name='reportform'),
    path('reports',views.reports, name='reports'),
    path('add_price/',views.add_price, name='add_price'),
    path('view_price',views.viewprice, name='viewprice'),
    path('store_price/',views.store_price, name='store_price'),
    path('res_reports',views.res_reports, name='res_reports'),
    path('customer_profile',views.customer_profile, name='customer_profile'),
    path('login/',views.login, name='login'),
    path('login_check/',views.login_check, name='login_check'),
    path('logout/',views.logout, name='logout'),
    path('my_profile/',views.my_profile, name='my_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update/<int:id>', views.update, name='update'),
    path('destroy/', views.destroy, name='destroy'),
    

]
