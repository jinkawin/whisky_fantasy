from django.db import models

# Location Model is used to store all the City Name as location_name
# Location Model is populated with the City Names obtained from data.json
class Location(models.Model):
    TEXT_MAX_LENGTH = 255
    location_name = models.CharField(max_length=TEXT_MAX_LENGTH, null=False ,unique=True)
