#this is my view.py file
from django.shortcuts import render

# Create your views here.
def home(request): #pyhton templates connect
	import json
	import requests #out of internet jayega

	api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=5&API_KEY=F30172B7-CBF0-432D-A320-7BB5F5487E48")
	#python things data se`
	try:
		api=json.loads(api_request.content)
		#try to get data is some error niche gaya
		#aqi is array of dictionary

	except Exception as e:
		api="Error...."

	return render(request,'home.html',{'api' : api})

def about(request): #pyhton templates connect
	return render(request,'about.html',{})