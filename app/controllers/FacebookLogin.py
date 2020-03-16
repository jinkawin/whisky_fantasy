from django.shortcuts import render

from app.models import Customer
from app.form import CustomerForm

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

def facebookLogin(request):
    context_dict = {}
    # if request.method == 'POST':

    return HttpResponse("Success")