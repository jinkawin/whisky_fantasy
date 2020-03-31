# Import External Libraries
from django.contrib.auth.models import User
from django.db import models
# Assign Internal Linkage Models
from app.tables.Customer import Customer

# PaymentInfo Model is used to store payment details of the User (Customer)
class PaymentInfo(models.Model):
    '''
    Variables:
        name_card:                  Owner Name of the Payment Card
        cardNo:                     Payment Card Number
        expiryMonth+expiryYear:     Expiry Year of the Payment Card
        cvv:                        Secret Code of the Payment Card
    '''
    # PaymentInfo Model link to User Model as Foreign Key to add as a Transaction record for the specific Customer
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name_card = models.CharField(max_length=40)
    cardNo = models.PositiveIntegerField()
    expiryYear = models.PositiveIntegerField()
    expiryMonth = models.PositiveIntegerField()
    cvv = models.PositiveIntegerField()
