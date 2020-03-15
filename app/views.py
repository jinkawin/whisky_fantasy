from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from app.forms import CustomerForm, UserProfileForm, MerchantForm
from app.models import Customer, UserProfile


def index(request):
    # customer = Customer()
    # customer.hello()
    return render(request, 'app/index.html')


def register_cust(request):
    registered = False
    if request.method == 'POST':
        user_form = CustomerForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = CustomerForm()
        profile_form = UserProfileForm()

    return render(request, 'app/register_customer.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def register_merchant(request):
    registered = False
    if request.method == 'POST':
        user_form = MerchantForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = MerchantForm()
        profile_form = UserProfileForm()
    return render(request, 'app/register_merchant.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def cust_login(request):
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


def merchant_login(request):
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


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        print(user_profile)

        user_profile.user.email = request.POST.get('email')
        user_profile.user.save()

        if 'picture' in request.FILES:
            user_profile.picture = request.FILES['picture']
            user_profile.save()

    return render(request, 'app/profile.html', {'profile': user_profile})


# @login_required
# def changepwd(request):
#     if request.method == 'GET':
#         form = ChangepwdForm()
#         return render(request, 'app/changepwd.html', {'form': form, })
#     else:
#         form = ChangepwdForm(request.POST)
#         if form.is_valid():
#             username = request.user.username
#             oldpassword = request.POST.get('oldpassword')
#             user = auth.authenticate(username=username, password=oldpassword)
#             if user is not None and user.is_active:
#                 newpassword = request.POST.get('newpassword1', '')
#                 user.set_password(newpassword)
#                 user.save()
#                 return render(reverse('app:myaccount'))
#             else:
#                 return render(request, 'app/changepwd.html', {'form': form, 'oldpassword_is_wrong': True})
#         else:
#             return render(request, 'app/changepwd.html', {'form': form, })

