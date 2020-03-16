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
            if user.is_active:
                try:
                    customer = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    customer = None
                if customer.role == '0':
                    login(request, user)
                    return redirect(reverse('app:myaccount'))
                else:
                    return HttpResponse('Please chose Merchant Login')

            else:
                return HttpResponse('Your account is disabled.')
        else:
            print(f"Invalid login details:{username},{password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/login_customer.html')