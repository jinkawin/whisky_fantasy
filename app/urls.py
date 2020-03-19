from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('facebook_login', views.facebookLogin, name='facebook_login'),
    path('cust_login/', views.custLogin, name='cust_login'),
    path('cust_register/', views.custRegister, name='cust_register'),
    path('merchant_login/', views.merchantLogin, name='merchant_login'),
    path('merchant_register/', views.merchantRegister, name='merchant_register'),
    path('myaccount/',views.profile,name='myaccount'),
    path('merchant_transaction/' , views.transaction, name='merchant_transaction'),
    path('add_product/',views.addProduct, name='add_product'),
    path('product/',views.productList,name='product')
]