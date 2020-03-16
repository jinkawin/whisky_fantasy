from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

def merchantRegister(request):
    return render(request, 'app/register_merchant.html')