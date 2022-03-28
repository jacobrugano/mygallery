from django.urls import path
# from django.conf.urls import url
from . import views 

urlpatterns = [
    path('', views.gallery, name='gallery'), # Our homepage
    path('photo/<str:pk>/', views.viewPhoto, name='photo'), # photo/<str:pk>/ to get photo by id or primary key
    path('add/', views.addPhoto, name='add'),
]
