from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import SignUpForm, EventForm
from .models import Event, RSVP  # Ensure RSVP is imported

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def event_index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            events = Event.objects.all()
        else:
            events = Event.objects.filter(Q(is_public=True) | Q(created_by=request.user))
    else:
        events = Event.objects.filter(is_public=True)

    category = request.GET.get('category')
    tags = request.GET.get('tags')

    if category:
        events = events.filter(category=category)
    if tags:
        events = events.filter(tags__icontains=tags)

    categories = Event.objects.values_list('category', flat=True).distinct()  # Get distinct categories

    # Add RSVP status to the context
    event_rsvp_status = {}
    for event in events:
        event_rsvp_status[event.id] = event.rsvp_set.filter(user=request.user).exists() if request.user.is_authenticated else False

    return render(request, 'events/index.html', {
        'events': events,
        'categories': categories,  # Pass categories to the template
        'tags': tags,
        'selected_category': category,
        'event_rsvp_status': event_rsvp_status,  # Pass RSVP status to the template
    })

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'log_in.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return redirect('home')

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)  # Include files for image upload
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event-index')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)  # Include files for image upload
        if form.is_valid():
            form.save()
            return redirect('event-index')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event-index')
    return render(request, 'events/delete_event.html', {'event': event})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    RSVP.objects.get_or_create(event=event, user=request.user)
    return redirect('event-index')
