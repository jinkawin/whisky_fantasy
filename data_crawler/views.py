from django.shortcuts import render

from data_crawler.models import Tweet

def index(request):
    return render(request, 'data_crawler/index.html')