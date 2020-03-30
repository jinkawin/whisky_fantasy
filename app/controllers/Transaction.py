from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.tables import Transaction, UserProfile


@login_required
def transaction(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.role == 1:
        transaction_mer = Transaction.objects.filter(merchant=request.user)
        print(transaction_mer)
    return render(request, 'app/mer_transaction.html', {'profile':profile,'trans_mer':transaction_mer})
    # else:
    #     transaction_cust = Transaction.objects.get(merchant=request.user)
    #     print(transaction_cust)
    #     return render(request, 'app/mer_transaction.html', {'transaction': transaction_cust})
