from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('cust_login', views.custLogin, name='cust_login'),
    path('cust_register', views.custRegister, name='cust_register'),
    path('merchant_login', views.merchantLogin, name='merchant_login'),
    path('merchant_register', views.merchantRegister, name='merchant_register'),
]