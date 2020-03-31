

from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from app.models import UserProfile

# merchantLogin is used for user to register as Merchant
def merchantLogin(request):
    # When user selects on 'Login' button
    if request.method == 'POST':
        # Username and Password entered will be validated
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # Check whether user exists or not
        if user:
            # If user exists, check whether user is currently active or not
            if user.is_active:
                try:
                    merchant = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    merchant = None
                # Determine user role whether Customer(0) or Merchant (1)
                if merchant.role == '1':
                    # Enable Merchant to proceed to the Transaction Page after Login Successfully
                    login(request, user)
                    return redirect(reverse('app:merchant_transaction'))
                else:
                    return HttpResponse('Please choose Customer Login') # When username is found under Customer
            else:
                return HttpResponse('Your account is disabled.') # When user account is suspended
        else:
            print(f"Invalid login details:{username},{password}")
            return HttpResponse("Invalid login details supplied.") # When incorrect username and password are entered
    else:
        return render(request, 'app/login_merchant.html')
