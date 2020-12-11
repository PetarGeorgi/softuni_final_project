from django.urls import path, re_path
from . import views
from .views import MyClubListView, MyClubDetailView, MyClubUpdateEvent, MyClubDeleteEvent, \
    MyClubCreateEvent, Event_view

urlpatterns = [
    path('', views.index, name='index'),
    path('add_venue/', views.add_venue, name='add-venue'),
    #path('events/', views.all_events, name='show-event'),
    path('getsubs/', views.list_subscribers, name='list-subscribers'),
    path('events_view/', Event_view.as_view()),
    path('allevents/', views.all_events, name='all-events'),
    path('event/<int:pk>', MyClubDetailView.as_view(), name='event-detail'),
    path('events/', MyClubListView.as_view(), name='show-events'),
    path('event/add/', MyClubCreateEvent.as_view(), name='add-event'),
    path('event/update/<int:pk>', MyClubUpdateEvent.as_view(), name='update-event'),
    path('event/delete/<int:pk>', MyClubDeleteEvent.as_view(), name='delete-event'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
    ]
