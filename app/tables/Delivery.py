# Import External Libraries
from django.contrib.auth.models import User
from django.db import models

from app.tables.Customer import Customer

# Delivery Model is used to store the delivery details of the user (Customer)
class Delivery(models.Model):
    """
        Variables:
            name:   Recipient Name of the Product Delivered to
            Address of Recipient is saved as the following format:
            addressOne, addressTwo, town_city, postcode
            phone:  UK Phone Number of the Recipient
    """
    # Delivery Model link to Customer Model as Foreign Key to add as a Transaction record for the specific Customer
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=40)
    addressOne = models.TextField(max_length=100)
    addressTwo = models.TextField(max_length=100, blank=True)
    town_city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=6)
    phone = models.PositiveIntegerField()
