from django.shortcuts import render

from app.forms.DeliveryForm import DeliveryForm


def delivery(request):
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        if delivery_form.is_valid():
            delivery_form.save()
    return render(request,'delivery_page.html')

