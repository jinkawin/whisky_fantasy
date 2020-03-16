from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

def profile(request):
    return render(request, 'app/profile.html')