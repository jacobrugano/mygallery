from django.contrib import admin

# Register your models here.
from django.contrib import admin

# To Register the models so as to appear in the Django admin page:
from .models import Photo, Category

admin.site.register(Category)
admin.site.register(Photo)