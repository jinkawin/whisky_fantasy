# Import External Libraries
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

# Import Internal Libraries
from app.forms.ProductForm import ProductForm
from app.tables import UserProfile
from app.tables.Transaction import Transaction
from app.tables.Whisky import Whisky, Location

'''
Overview:
    productList:    list out all the Whisky [Merchant]
    search_page:    Sort all Whisky according to the Price in ascending order [Customer]
    search_product: render product list for search page when searching for some products [Customer]
    product_detail: render product detail page for the specific Whisky [Customer]
    addProduct:     to add new whisky for sale [Merchant]
    editProduct:    to edit the existing whisky for sale [Merchant]
    set_status:     void the existing Whisky [Merchant], product become unavailable for sale
'''

@login_required
def productList(request):  # render product list for merchant
    profile = UserProfile.objects.get(user=request.user)
    product = Whisky.objects.filter(merchant=request.user).order_by('-id')
    print(product)

    return render(request, 'app/product.html', {'product': product, 'profile': profile})


def search_page(request):  # render product list for search page
    product = Whisky.objects.filter(whisky_status=1).order_by('whisky_price')
    print(product)

    return render(request, 'app/search_by_price.html', {'product': product})


def search_product(request):  # render product list for search page when searching for some products
    if request.method == 'POST':
        query = request.POST.get('query')
        product = Whisky.objects.filter(whisky_name__icontains=query, whisky_status=1)
        print(product)
        return render(request, 'app/search_by_price.html', {'product': product})


def product_detail(request):  # render product details when browsing a single product
    if request.method == 'GET':
        profile = UserProfile.objects.get(user=request.user)
        product_id = request.GET.get('product_id')
        product = Whisky.objects.get(id=product_id)
        return render(request, 'app/detail_page.html', {'product': product, 'profile': profile})
    else:
        product_id = request.POST.get('whisky_id')
        product = Whisky.objects.get(id=product_id)
        quantity = request.POST.get('trans_quantity')

        # create a transaction when post a request and reverse to next page
        transaction_info = Transaction.objects.create(
            customer=request.user,
            whisky=product,
            merchant=product.merchant.username,
            trans_price=product.whisky_price,
            trans_quantity=quantity,
            trans_amount=product.whisky_price * int(quantity),
            trans_status=0,
            trans_time=timezone.now(),
        )
        return redirect(reverse('app:delivery', kwargs={'trans_id': transaction_info.id}))


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
            print('--------- Error -------------')
            print(product.errors)
    else:
        product = ProductForm()
    return render(request, 'app/add_product.html', {'product': product, 'locations': locations, 'profile': profile})


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
        return render(request, 'app/edit_product.html',
                      {'product': product, 'locations': locations, 'profile': profile})


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
