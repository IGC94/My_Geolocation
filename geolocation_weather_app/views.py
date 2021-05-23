from django.shortcuts import render
import requests
import json
import urllib.request

# Create your views here.

def GeoLocation(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)

    return render(request, 'geolocation.html', {'data':location_data})
