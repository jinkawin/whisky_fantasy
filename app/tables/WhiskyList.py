from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class WhiskyList(models.Model):
    NAME_MAX_LENGTH = 128

    whisky_category_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
