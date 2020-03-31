from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.tables import UserProfile

# profile allows users to view and edit their personal details
@login_required
def profile(request):
    # Connect to UserProfile Model to obtain user details
    user_profile = UserProfile.objects.get(user=request.user)
    # When user intends to submit their changes within their user profile
    if request.method == 'POST':
        print(user_profile)
        # save the changes of their email address
        user_profile.user.email = request.POST.get('email')
        user_profile.user.save()
        # Only update their profile picture if any changes
        if 'picture' in request.FILES:
            user_profile.picture = request.FILES['picture']
            user_profile.save()

    return render(request, 'app/profile.html', {'profile': user_profile})
