from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.event_index, name='event-index'),
    path('signup/', views.sign_up, name='sign-up'),
    path('login/', views.log_in, name='log-in'),
    path('logout/', views.log_out, name='log-out'),
    path('events/add/', views.add_event, name='add-event'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit-event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete-event'),
]
