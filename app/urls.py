from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('facebook_login', views.facebookLogin, name='facebook_login'),
    path('twitter_login', views.twitterLogin, name='twitter_login'),
    path('cust_login/', views.custLogin, name='cust_login'),
    path('cust_register/', views.custRegister, name='cust_register'),
    path('merchant_login/', views.merchantLogin, name='merchant_login'),
    path('merchant_register/', views.merchantRegister, name='merchant_register'),
    path('myaccount/',views.profile,name='myaccount'),
    path('merchant_transaction/' , views.transaction, name='merchant_transaction'),
    path('add_product/',views.addProduct, name='add_product'),
    path('product/',views.productList,name='product'),
    path('product_status/',views.set_status, name='product_status'),
    path('edit_product/',views.editProduct,name='edit_product'),
    # The following are urls specialised for frontend only
    path('search_by_price/',views.searchPrice, name='searchPrice'),
    # path('search_by_location/',views.searchLocation, name='search_by_location'),
    # path('detail_page/',views.detailsProduct, name='detail_page'),
    # path('delivery_page/',views.deliveryDetails,name='delivery'),
    # path('payment_page/',views.payment,name='payment'),
]
