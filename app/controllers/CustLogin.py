from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from app.tables import UserProfile

# custLogin is to validate username and password with User Model through UserProfile Model
def custLogin(request):
    context_dict = {}
    # When user select on 'Login' button
    if request.method == 'POST':
        # Obtain username and password entered and validate them
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # If user exists, check whether user is currently active or not
        if user:
            if user.is_active:
                try:
                    customer = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    customer = None
                # Determine user role whether Customer(0) or Merchant (1)
                if customer.role == '0':
                    # Enable Customer to proceed to the Search Page after Login Successfully
                    login(request, user)
                    return redirect(reverse('app:search_by_price'))
                else:
                    return HttpResponse('Please choose Merchant Login') # When username is found under Merchant
            else:
                return HttpResponse('Your account is disabled.') # When user account is suspended
        else:
            print(f"Invalid login details:{username},{password}")
            return HttpResponse("Invalid login details supplied.") # When incorrect username and password are entered
    else:
        return render(request, 'app/login_customer.html')
