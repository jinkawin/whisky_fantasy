from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.tables import Transaction, UserProfile


@login_required
def transaction(request):
    # user = UserProfile.objects.get(user=request.user)
    #
    # if user.role == 0:
    #     transaction_mer = Transaction.objects.get(customer=request.user)
    #     print(transaction_mer)
        return render(request, 'app/mer_transaction.html', {})
    # else:
    #     transaction_cust = Transaction.objects.get(merchant=request.user)
    #     print(transaction_cust)
    #     return render(request, 'app/mer_transaction.html', {'transaction': transaction_cust})
