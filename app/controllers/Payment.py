from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms import PaymentForm
from app.tables import Transaction
from app.tables.Whisky import Whisky

# payment validates the payment details and create new Transaction data if successful
def payment(request, trans_id):
    # Obtain the transaction id from Delivery Page
    trans_info = Transaction.objects.get(id=trans_id)
    # Obtain product id
    product = Whisky.objects.get(id=trans_info.whisky.id)
    paid = False
    # When user select on 'Pay' button
    if request.method == 'POST':
        # Check whether product is available for purchase or not
        if product.whisky_quantity >= trans_info.trans_quantity:
            payment_form = PaymentForm(request.POST)
            if payment_form.is_valid():
                # Save Payment details into PaymentForm
                payment_info = payment_form.save(commit=False)
                payment_info.customer = request.user
                payment_info.save()
                # Save Transaction details
                trans_info.trans_status = 1
                trans_info.save()

                paid = True
                # Update quantity of product left after purchased
                product.whisky_quantity = product.whisky_quantity - trans_info.trans_quantity

                # Save all changes into the Whisky model
                product.save()

                return redirect(reverse('app:customer_transaction'))

            else:
                print(payment_form.errors)
        else:
            return HttpResponse('The stock of this product is not enough. Please choose another product.')

    else:
        payment_form = PaymentForm()
    return render(request, 'app/payment_page.html', {'payment_form': payment_form,'product':product})
