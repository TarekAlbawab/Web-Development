from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def default_map(request):
    mapbox_access_token = 'your token'
    return render(request, 'map.html', {mapbox_access_token:mapbox_access_token})
