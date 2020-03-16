from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

def merchantLogin(request):
    return render(request, 'app/login_merchant.html')