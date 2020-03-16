from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

def custRegister(request):
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST)

        if customerForm.is_valid():
            customer = customerForm.save()

            customer.set_password(customer.password)
            customer.save()

            print('---------- SAVED ----------')

            # TODO: set user's session

        else:
            print('---------- ERROR ----------')
            print(customerForm.errors)
            print(request.POST)
            print('---------- /ERROR ----------')
    return render(request, 'app/register_customer.html')