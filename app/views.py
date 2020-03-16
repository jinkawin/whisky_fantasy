from django.shortcuts import render
from app.models import Customer

def index(request):
    return render(request, 'app/index.html')

def custLogin(request):
    return render(request, 'app/login_customer.html')

def custRegister(request):
    return render(request, 'app/register_customer.html')

def merchantLogin(request):
    return render(request, 'app/login_merchant.html')

def merchantRegister(request):
    return render(request, 'app/register_merchant.html')

def profile(request):
    return render(request, 'app/profile.html')