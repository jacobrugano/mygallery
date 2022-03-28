from django.shortcuts import render
from .models import Category, Photo

# Create your views here.
def gallery(request):
    categories = Category.objects.all() #To query the Database for categories from the Category model
    photos = Photo.objects.all()  #To query the Database for photos from the Photo model
    
    context = {'categories':categories, 'photos':photos}
    return render(request, 'photos/gallery.html', context)
                                    # 'photos/gallery.html'...the path whwre we will output
                                    # context.....a variable holding the data we will output

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk) # get...bcos we are not capturing everything
                                     # id=pk...we capture the photo by the id which is the primary key
    return render(request, 'photos/photo.html')

def addPhoto(request):
    return render(request, 'photos/add.html')