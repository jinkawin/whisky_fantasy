import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app.tables.Location import Location


def searchLocation(request):
    response_data = {}

    locations = Location.objects.filter(location_name__contains=request.GET.get('key'))
    response_data['locationList'] = [ location.location_name for location in locations]

    return HttpResponse(json.dumps(response_data), content_type="application/json")