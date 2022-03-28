from django.shortcuts import render
from .models import Category, Photo

# Create your views here.
def gallery(request):
    categories = Category.objects.all() #To query the Database
    return render(request, 'photos/gallery.html', {'categories':categories})

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')

def addPhoto(request):
    return render(request, 'photos/add.html')