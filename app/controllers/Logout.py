from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('app:index'))