from django.shortcuts import render
from app.models import Customer

from app.form import CustomerForm

def index(request):
    return render(request, 'app/index.html')

def custLogin(request):
    return render(request, 'app/login_customer.html')

def custRegister(request):
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST)

        if customerForm.is_valid():
            customerForm.save(commit=True)

            print('---------- SAVED ----------')

            # TODO: set user's session

        else:
            print('---------- ERROR ----------')
            print(customerForm.errors)
            print(request.POST)
            print('---------- /ERROR ----------')
    return render(request, 'app/register_customer.html')

def merchantLogin(request):
    return render(request, 'app/login_merchant.html')

def merchantRegister(request):
    return render(request, 'app/register_merchant.html')

def profile(request):
    return render(request, 'app/profile.html')