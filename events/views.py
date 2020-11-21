import calendar
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render
from calendar import HTMLCalendar

# Create your views here.
from events.models import Event


def index(request, year=date.today().year, month=date.today().month):
    # t = date.today()
    # month = date.strftime(t, '%b')
    # year = t.year
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" %(month_name, year)
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    #return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,cal))
    return render(request, 'events/calendar_base.html', {'title': title, 'cal': cal})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})