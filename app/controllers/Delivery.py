from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms.DeliveryForm import DeliveryForm
from app.tables import Transaction

# delivery is used to validate and input data into Transaction Model
def delivery(request,trans_id):
    trans_info = Transaction.objects.get(id=trans_id)
    product_id = trans_info.whisky.id
    # When user select on 'Confirm' button
    if request.method == 'POST':
        # link to DeliveryForm
        delivery_form = DeliveryForm(request.POST)
        # Check whether DeliveryForm is valid or not
        if delivery_form.is_valid():
            # save details by relating to Customer model
            deliveryInfo = delivery_form.save(commit=False)
            deliveryInfo.customer = request.user
            deliveryInfo.save()
            print(deliveryInfo)
            # save address details to Transaction Model
            trans_info.trans_address = deliveryInfo
            trans_info.save()
            print(trans_info)
            return redirect(reverse('app:payment',kwargs={'trans_id': trans_id}))
        else:
            print(delivery_form.errors)
    else:
        delivery_form = DeliveryForm()
    return render(request, 'app/delivery_page.html', {'delivery_form': delivery_form,'product_id':product_id})
