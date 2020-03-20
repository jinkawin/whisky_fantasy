from django.shortcuts import render


from django.contrib.auth.decorators import login_required

from app.tables import UserProfile


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