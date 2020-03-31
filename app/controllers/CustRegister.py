from django.shortcuts import render, redirect

from app.forms import CustomerForm, UserProfileForm

# custRegister allows user to register as Customer
def custRegister(request):
    registered = False
    # after user select 'Sign Up' button, data entered will be sent to CustomerForm and UserProfileForm
    if request.method == 'POST':
        user_form = CustomerForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        print(user_form)
        # Validate user details with CustomerForm and UserProfileForm successfully
        if user_form.is_valid() and profile_form.is_valid():
            # Save user details into CustomerForm
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # Save user details into UserProfileForm
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)  # Print related errors
    else:
        user_form = CustomerForm()
        profile_form = UserProfileForm()

    return render(request, 'app/register_customer.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
