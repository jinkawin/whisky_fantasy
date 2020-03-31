from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms.DeliveryForm import DeliveryForm
from app.tables import Transaction


def delivery(request,trans_id):
    trans_info = Transaction.objects.get(id=trans_id)
    product_id = trans_info.whisky.id
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        if delivery_form.is_valid():
            deliveryInfo = delivery_form.save(commit=False)
            deliveryInfo.customer = request.user
            deliveryInfo.save()
            trans_info.trans_address = deliveryInfo
            trans_info.save()
            print(deliveryInfo)
            print(trans_info)
            return redirect(reverse('app:payment',kwargs={'trans_id': trans_id}))
        else:
            print(delivery_form.errors)
    else:
        delivery_form = DeliveryForm()
    return render(request, 'app/delivery_page.html', {'delivery_form': delivery_form,'product_id':product_id})
