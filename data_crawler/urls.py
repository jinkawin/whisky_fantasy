from django.urls import path
from data_crawler import views

app_name = 'data_crawler'

urlpatterns = [
    path('', views.index, name='index')
]