
from django.shortcuts import render, redirect

from app.forms import CustomerForm, UserProfileForm

def custRegister(request):
    registered = False
    if request.method == 'POST':
        user_form = CustomerForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        print(user_form)

        if user_form.is_valid() and profile_form.is_valid():
            print("yes?")
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