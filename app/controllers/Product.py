from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms.ProductForm import ProductForm
from app.tables.Merchant import Merchant
from app.tables.Whisky import Whisky


@login_required
def productList(request):

    product = Whisky.objects.filter(merchant=request.user)
    print(product)

    return render(request, 'app/product.html', {'product': product})

@login_required
def addProduct(request):
    if request.method == 'POST':
        product = ProductForm(request.POST, request.FILES)
        merchant = User.objects.get(username=request.POST.get('merchant'))
        product.merchant = merchant
        if product.is_valid():
            product.save()
            return redirect(reverse('app:product'))

        else:
            print(product.errors)
    else:
        product = ProductForm()

    return render(request, 'app/add_product.html', {'product': product})



