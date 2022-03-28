from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    # class Meta:
    #     verbose_name = 'Category'
    #     verbose_name_plural = 'Categories'

    # user = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    # class Meta:
    #     verbose_name = 'Photo'
    #     verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
                #  on_delete=models.SET_NULL...so that deleting does not delete all photos with that key.
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
                # TextField...does not need limits of letters to use like CharField 

    def __str__(self):
        return self.description