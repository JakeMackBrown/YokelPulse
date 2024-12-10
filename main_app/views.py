from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def event_index(request):
    return render(request, 'events/index.html', {'events': events})


class Event:
    def __init__(self, title, description, date, location, category, tags):
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        self.category = category
        self.tags = tags

# Create a list of Cat instances
events = [
    Event('Machine Girl concert', 'Machine Girl live in concert for their new album', 'October 25th', 'The Firebird', 'Concert', 'Electronic, Grungy, Videogame music')
]
