from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms.ProductForm import ProductForm
from app.tables import UserProfile
from app.tables.Whisky import Whisky, Location

import json


@login_required
def productList(request):
    profile = UserProfile.objects.get(user=request.user)
    product = Whisky.objects.filter(merchant=request.user).order_by('-id')
    print(product)

    return render(request, 'app/product.html', {'product': product,'profile':profile})


def search_page(request):
    product = Whisky.objects.all()
    print(product)

    return render(request, 'app/search_by_price.html', {'product': product})


def product_detail(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = Whisky.objects.get(id=product_id)
        return render(request, 'app/detail_page.html', {'product': product,'profile':profile})


@login_required
def addProduct(request):
    profile = UserProfile.objects.get(user=request.user)
    locationObj = Location.objects.all()
    locations = json.dumps([location.location_name for location in locationObj])

    print(locations)
    if request.method == 'POST':
        product = ProductForm(request.POST, request.FILES)
        print(product)
        if product.is_valid():
            product.save()
            return redirect(reverse('app:product'))
        else:
            print('--------- Errro -------------')
            print(product.errors)
    else:
        product = ProductForm()
    return render(request, 'app/add_product.html', {'product': product, 'locations': locations,'profile':profile})


@login_required
def editProduct(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        product_id = request.POST.get('id')
        print(product_id)
        if product_id is not None:
            product = Whisky.objects.get(id=product_id)
            product.whisky_name = request.POST.get('whisky_name')
            product.whisky_price = request.POST.get('whisky_price')
            product.whisky_quantity = request.POST.get('whisky_quantity')
            product.whisky_description = request.POST.get('whisky_description')
            picture = request.FILES.get('whisky_img')
            if picture is not None:
                product.whisky_img = request.FILES.get('whisky_img')
            product.whisky_location = Location.objects.get(location_name=request.POST.get('whisky_location'))
            product.save()
            return redirect(reverse('app:product'))

    else:
        product_id = request.GET.get('product_id')
        product = Whisky.objects.get(id=product_id)
        locationObj = Location.objects.all()
        locations = json.dumps([location.location_name for location in locationObj])
        return render(request, 'app/edit_product.html', {'product': product, 'locations': locations,'profile':profile})


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
