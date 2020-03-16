from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

from django.contrib.auth import authenticate, login, logout

def custLogin(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
    return render(request, 'app/login_customer.html')