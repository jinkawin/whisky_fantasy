from django.db import models

from app.tables.Customer import Customer


class Delivery(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    addressOne = models.TextField(max_length=100)
    addressTwo = models.TextField(max_length=100, blank=True)
    town_city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=6)
    phone = models.PositiveIntegerField()
