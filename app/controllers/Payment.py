from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms import PaymentForm
from app.tables import Transaction
from app.tables.Whisky import Whisky


def payment(request, trans_id):
    trans_info = Transaction.objects.get(id=trans_id)
    product = Whisky.objects.get(id=trans_info.whisky.id)
    paid = False
    if request.method == 'POST':
        if product.whisky_quantity >= trans_info.trans_quantity:
            payment_form = PaymentForm(request.POST)
            if payment_form.is_valid():
                payment_info = payment_form.save(commit=False)
                payment_info.customer = request.user
                payment_info.save()
                trans_info.trans_status = 1
                trans_info.save()
                paid = True
                product.whisky_quantity = product.whisky_quantity - trans_info.trans_quantity
                product.save()

                return render(request, 'app/payment_page.html', {'paid': paid})

            else:
                print(payment_form.errors)
        else:
            return HttpResponse('The stock of this product is not enough, please choose another product')

    else:
        payment_form = PaymentForm()
    return render(request, 'app/payment_page.html', {'payment_form': payment_form,'product':product})
