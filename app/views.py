from django.shortcuts import render
from app.models import Customer

def index(request):
    customer = Customer()
    customer.hello()
    return render(request, 'app/index.html')