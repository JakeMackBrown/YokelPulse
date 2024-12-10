from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.event_index, name='event-index'),
    path('signup/', views.sign_up, name='sign-up'),
    path('login/', views.log_in, name='log-in'),
    path('logout/', views.log_out, name='log-out'),
]
