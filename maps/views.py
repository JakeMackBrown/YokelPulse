from django.shortcuts import render

def map_view(request):
    events = [
        {"name": "Community Fair", "lat": 38.6270, "lng": -90.1994},
        {"name": "Art Festival", "lat": 38.6300, "lng": -90.2000},
    ]
    context = {
        'google_maps_api_key': 'AIzaSyDOyVeFfj0x8OfpaSaHXdVRRkse6j666zU', 
        'events': events,
    }
    return render(request, 'maps/map.html', context)
