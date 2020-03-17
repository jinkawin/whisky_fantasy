from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from app.models import UserProfile

def merchantLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    merchant = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    merchant = None
                if merchant.role == '1':
                    login(request, user)
                    return redirect(reverse('app:myaccount'))
                else:
                    return HttpResponse('Please chose Customer Login')

            else:
                return HttpResponse('Your account is disabled.')
        else:
            print(f"Invalid login details:{username},{password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/login_merchant.html')