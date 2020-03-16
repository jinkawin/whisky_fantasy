from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('facebook_login', views.facebookLogin, name='facebook_login'),
    path('cust_login', views.custLogin, name='cust_login'),
    path('cust_register', views.custRegister, name='cust_register'),
    path('merchant_signup', views.merchantLogin, name='merchant_signup'),
    path('register_merchant', views.merchantRegister, name='register_merchant'),
    path('myaccount/',views.profile,name='myaccount'),
]