# Import External Libraries
from django.contrib.auth.models import User
from django.db import models
# Assign Internal Linkage Models
from app.tables.Location import Location
from app.tables.WhiskyList import WhiskyList

# Whisky Model is used to store the product details of the Whisky
class Whisky(models.Model):
    '''
    Variables:
        whisky_location: link to Location Model and obtain location_name
        whisky_name: Name of the Whisky
        whisky_description: Description of the Whisky
        whisky_price: Price in (£) of the Whisky_Name
        whisky_quantity: Quantity of the Whisky
        whisky_status: 1, Available; 0, Unavailable
        whisky_img_link: Path link of the Whisky Image
        whisky_img: Image of the Whisky are saved to media/product_images directory
        merchant: Seller of the Whisky
    '''
    TEXT_MAX_LENGTH = 255

    whisky_location = models.ForeignKey(Location, on_delete=models.CASCADE, to_field="location_name")
    whisky_name = models.CharField(max_length=TEXT_MAX_LENGTH, null=False)
    whisky_description = models.CharField(max_length=TEXT_MAX_LENGTH, null=False)
    whisky_price = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0.00)
    whisky_quantity = models.PositiveIntegerField(default=1, null=False)
    whisky_status = models.IntegerField(default=1, null=False)
    whisky_img_link = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)
    whisky_img = models.ImageField(upload_to='product_images',blank=True)
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Whisky, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Whiskies'

    def __str__(self):
        return self.whisky_name
