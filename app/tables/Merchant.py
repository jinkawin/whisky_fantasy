from django.db import models

# Merchant Model is used to store the details of Users at the Backend
class Merchant(models.Model):
    """
        Variables:
            username    - store username of Customer which will be used for login verification
            password    - store password in Encrypted Hash Format which will be used for login verification
            cust_email  - store email of Customer
    """
    TEXT_MAX_LENGTH = 255
    
    merchant_username = models.CharField(max_length=TEXT_MAX_LENGTH, null=False, unique=True)
    merchant_password = models.CharField(max_length=TEXT_MAX_LENGTH, null=False)
    merchant_email = models.EmailField(max_length=TEXT_MAX_LENGTH, null=False)
