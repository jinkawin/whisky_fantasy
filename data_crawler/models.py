from django.db import models

class Tweet(models.Model):
    name = models.CharField(max_length=50)