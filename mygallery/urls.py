"""mygallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings    #To access settings file
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
# To register our url file into the app
    path('', include('photos.urls')), #going into photos app then into urls file
]

#To direct the app where to find media items like images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #To direct the app where to find the images

#To direct the app where to find media and other files like css
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
