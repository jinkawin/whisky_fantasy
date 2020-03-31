from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from app.tables import Transaction, UserProfile
from app.tables.Whisky import Whisky


@login_required
def transaction(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'GET':

        if profile.role == "1":

            transaction_details = Transaction.objects.filter(merchant=request.user).order_by('-id')
            print(transaction_details)
            return render(request, 'app/mer_transaction.html', {'profile': profile, 'transaction': transaction_details})
        else:
            transaction_details = Transaction.objects.filter(customer=request.user).order_by('-id')
            return render(request, 'app/cust_transaction.html', {'profile': profile, 'transaction': transaction_details})


