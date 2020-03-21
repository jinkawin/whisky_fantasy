import json

from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from libs.Twitter import Twitter

from app.models import Customer, UserProfile
from app.form import CustomerForm, UserProfileForm

def twitterLogin(request):
    response_data = {}

    callback = request.build_absolute_uri(reverse('app:twitter_login'))
    twitter = Twitter(callback)

    if "oauth_token" in request.GET:
        # Callback from Twiteer
        me = twitter.me()

        role = request.role = '0'
        twId = request.cust_tw_id = me['id']
        username = request.username = me['screen_name']
        email = request.email = None

        data = {
            'role': role,
            'cust_tw_id': twId,
            'username': username,
            'email': email,
            'password': settings.SECRET_VALUE
        }

        try:
            _user = UserProfile.objects.get(cust_tw_id=twId)

        except UserProfile.DoesNotExist:
            _user = None

        if _user:
            user = authenticate(username=_user.user.username, password=settings.SECRET_VALUE)
            login(request, user)
            response_data['message'] = 'Success'
            response_data['isSuccess'] = True
            print(' --------------- RESULT ---------------')
            print('User is existed and alredy logged in')

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

                profile.cust_tw_id = twId

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
        return twitter.login()

    return redirect(reverse('app:myaccount'))