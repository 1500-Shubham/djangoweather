from django.shortcuts import render

# Create your views here.
def home(request): #pyhton templates connect
	return render(request,'home.html',{})
def about(request): #pyhton templates connect
	return render(request,'about.html',{})