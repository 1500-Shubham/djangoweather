from django.urls import path
from . import views # .means lookup same folder

urlpatterns = [
    path('', views.home,name="home"), #all webpage
    path('about.html', views.about,name="about"), #all webpage
]
  