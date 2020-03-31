# Import External Libraries
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# WhiskyList is used to classify the Whisky Products into Categories
class WhiskyList(models.Model):
    NAME_MAX_LENGTH = 128

    whisky_category_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0

        self.slug = slugify(self.whisky_category_name)
        super(WhiskyList, self).save(*args, **kwargs)

    def __str__(self):
        return self.whisky_category_name
