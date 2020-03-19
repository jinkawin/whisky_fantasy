from django.contrib import admin


from app.models import UserProfile

# Register your models here.
from app.tables.Whisky import Whisky

admin.site.register(UserProfile)
admin.site.register(Whisky)