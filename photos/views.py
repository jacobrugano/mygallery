from django.shortcuts import render,redirect
from .models import Category, Photo

# Create your views here.
def gallery(request):
    # categories = Category.objects.all() #To query the Database for categories from the Category model
    # photos = Photo.objects.all()  #To query the Database for photos from the Photo model

    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = {'categories':categories, 'photos':photos}
    return render(request, 'photos/gallery.html', context)
                                    # 'photos/gallery.html'...the path whwre we will output
                                    # context.....a variable holding the data we will output
                                    # Note: The curly braces cover the entire data to be outputted

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk) # get...bcos we are not capturing everything
                                     # id=pk...we capture the photo by the id which is the primary key
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all() #To query the Database for the photos we are adding
   

    if request.method == 'POST': #To check if the request type is a POST, and if so, go ahead and create an image.
            data = request.POST   # But we first get the form data
            image = request.FILES.get('image') #We also get the image. The name ...image... is the name of the UPLOAD button
           
            if data['category'] != 'none':
                category = Category.objects.get(id=data['category'])
            elif data['category_new'] != '':
                category, created = Category.objects.get_or_create(
                    # user=user,
                    name=data['category_new'])
            else:
                category = None

            # for image in images:
                photo = Photo.objects.create(
                    category=category,
                    description=data['description'],
                    image=image,
                )

            return redirect('gallery')
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)