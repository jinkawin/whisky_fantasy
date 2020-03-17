import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from app.models import Customer, UserProfile
from app.form import CustomerForm, UserProfileForm

# <QueryDict: {'role': ['0'], 'cust_email': ['jinkawin.pho@hotmail.com'], 'username': ['jinkawin'], 'password': ['12345'], 'cust_password_c': ['12345']}>

def facebookLogin(request):
    response_data = {'isSuccess': False}
    if request.method == 'POST':
        role = request.POST.get('role')
        fbId = request.POST.get('cust_fb_id')
        username = request.POST.get('username')
        email = request.POST.get('email')

        data = {
            'role': role,
            'cust_fb_id': fbId,
            'username': username,
            'email': email,
            'password': settings.SECRET_VALUE
        }

        try:
            _user = UserProfile.objects.get(cust_fb_id=fbId)

        except UserProfile.DoesNotExist:
            _user = None

        if _user:
            user = authenticate(username=_user.user.username, password=settings.SECRET_VALUE)
            login(request, user)
            response_data['message'] = 'Success'
            response_data['isSuccess'] = True
            print(' --------------- RESULT ---------------')
            print('User is existed and alredy logged in')

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:

            user_form = CustomerForm(data)
            profile_form = UserProfileForm(data)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.cust_fb_id = fbId

                profile2 = profile.save()
                registered = True

                user = authenticate(username=user.username, password=settings.SECRET_VALUE)
                login(request, user)

                response_data['message'] = 'Success'
                response_data['isSuccess'] = True

                print(' --------------- RESULT ---------------')
                print('Create a new user')
            else:
                response_data['message'] = {'user': user_form.errors, 'profile': profile_form.errors}
                print(' --------------- Error ---------------')
                print(user_form.errors, profile_form.errors)

    else:
        response_data['message'] = 'Link not found'

    return HttpResponse(json.dumps(response_data), content_type="application/json")