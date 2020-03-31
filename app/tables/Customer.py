# Import External Libraries
from django.db import models
from django.contrib.auth.models import AbstractUser

# Customer Model is used to store the details of Users at the Frontend
class Customer(models.Model):
    """
        Variables:
            username    - store username of Customer which will be used for login verification
            password    - store password in Encrypted Hash Format which will be used for login verification
            cust_email  - store email of Customer
    """
    TEXT_MAX_LENGTH = 255
    username = models.CharField(max_length=TEXT_MAX_LENGTH, null=False, unique=True)
    password = models.CharField(max_length=TEXT_MAX_LENGTH, null=False)
    cust_email = models.EmailField(max_length=TEXT_MAX_LENGTH, null=False)
    # cust_fb_id = models.CharField(max_length=255, blank=True, null=True)
    # cust_tw_id = models.CharField(max_length=255, blank=True, null=True)
