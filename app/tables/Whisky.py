from django.db import models

class Whisky(models.Model):
    location = models.ForeignKey(Location)
    whisky_name = models.CharField(max_length=255, null=False)
    whisky_description = models.CharField(max_length=255, null=False)
    whisky_status = models.CharField(max_length=255, null=False)
    whisky_status = models.CharField(max_length=255, default=1, null=False)
    whisky_img_link = models.CharField(max_length=255)