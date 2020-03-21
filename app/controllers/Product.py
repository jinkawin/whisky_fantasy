from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms.ProductForm import ProductForm
from app.tables.Whisky import Whisky


@login_required
def productList(request):
    product = Whisky.objects.filter(merchant=request.user)
    print(product)

    return render(request, 'app/product.html', {'product': product})


def search_page(request):
    product = Whisky.objects.all()
    print(product)

    return render(request, 'app/search_by_price.html', {'product': product})

def product_detail(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = Whisky.objects.get(id=product_id)
        return render(request, 'app/edit_product.html', {'product': product})


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


@login_required
def editProduct(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        print(product_id)
        if product_id is not None:
            product = Whisky.objects.get(id=product_id)
            product.whisky_name = request.POST.get('whisky_name')
            product.whisky_price = request.POST.get('whisky_price')
            product.whisky_quantity = request.POST.get('whisky_quantity')
            product.whisky_description = request.POST.get('whisky_description')
            product.whisky_img = request.FILES.get('whisky_img')
            product.location = request.POST.get('location')
            print(product.location)
            product.save()
            return redirect(reverse('app:product'))

    else:
        product_id = request.GET.get('product_id')
        product = Whisky.objects.get(id=product_id)
        return render(request, 'app/edit_product.html', {'product': product})


@login_required
def set_status(request):
    product_id = request.GET['id']
    status = request.GET['status']

    try:
        product = Whisky.objects.get(id=product_id)
    except Whisky.DoseNoExist:
        return HttpResponse(-1)
    except ValueError:
        return HttpResponse(-1)
    product.whisky_status = status
    product.save()
    return render(request, 'app/product.html', {'id': product_id, 'status': status})
