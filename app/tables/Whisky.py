from django.contrib.auth.models import User
from django.db import models


from app.tables.Location import Location
from app.tables.Merchant import Merchant


class Whisky(models.Model):
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location = models.CharField(max_length=255,blank=True)
    whisky_name = models.CharField(max_length=255, null=False)
    whisky_description = models.CharField(max_length=255, null=False)
    # whisky_status = models.CharField(max_length=255, null=False)
    whisky_price = models.DecimalField(max_digits=20,decimal_places=2, null=False, default=0.0)
    whisky_quantity = models.PositiveIntegerField()
    whisky_status = models.IntegerField(default=1, null=False)
    whisky_img_link = models.CharField(max_length=255 , blank=True)
    whisky_img = models.ImageField(upload_to='product_images',blank=True)
    merchant = models.ForeignKey(User,on_delete=models.CASCADE)