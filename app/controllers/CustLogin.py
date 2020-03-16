from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

from django.contrib.auth import authenticate, login, logout

def custLogin(request):
    context_dict = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            print('---------------- LOGGED IN ----------------')
        else:
            print('---------------- ERROR ----------------')
            context_dict['err_msg'] = "username or password is incorrect"

    return render(request, 'app/login_customer.html', context=context_dict)