# Import External Libraries
from django.contrib.auth.models import User
from django.db import models
# Assign Internal Linkage Models
from app.tables import Customer, Merchant

# UserProfile Model is used to differentiate users whether Merchant or Customer
class UserProfile(models.Model):
    '''
    Variables:
        cust_fb_id: stores Facebook ID where customer register through Facebook API
        cust_tw_id: stores Twitter ID where customer register through Twitter API
        role: 0, Customer; 1, Merchant
        picture_img_link
        picture
    '''
    TEXT_MAX_LENGTH = 255
    # UserProfile Model is linked to Django Default User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cust_fb_id = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True, null=True)
    cust_tw_id = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True, null=True)
    role = models.CharField(max_length=1, choices=(('0', 'customer'), ('1', 'merchant')))
    picture_img_link = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
