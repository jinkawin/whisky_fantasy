from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

def index(request):
    return render(request, 'app/index.html')