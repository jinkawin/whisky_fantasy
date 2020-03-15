from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('cust_signup/', views.register_cust, name='cust_signup'),
    path('merchant_signup/', views.register_merchant, name='merchant_signup'),
    path('cust_login/', views.cust_login, name='cust_login'),
    path('merchant_login/', views.merchant_login, name='merchant_login'),
    path('myaccount/',views.profile,name='myaccount'),
    # path('changepsw/',views.changepwd,name='changepsw')

]
