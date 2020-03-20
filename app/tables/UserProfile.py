from django.contrib.auth.models import User
from django.db import models

from app.tables import Customer


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cust_fb_id = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=1, choices=(('0', 'customer'), ('1', 'merchant')))
    picture = models.ImageField(upload_to='profile_images', blank=True)



    def __str__(self):
        return self.user.username