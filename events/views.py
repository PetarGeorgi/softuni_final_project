import calendar
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from  django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from events.forms import VenueForm, EventForm
from events.models import Event, MyClubUser, Venue


def index(request, year=date.today().year, month=date.today().month):
    # t = date.today()
    # month = date.strftime(t, '%b')
    # year = t.year
    year = int(year)
    month = int(month)
    #assert False
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


@login_required(login_url=reverse_lazy('login'))
def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html',
                  {'form': form, 'submitted': submitted}
                  )
def all_events(request):
    EventsFormSet = modelformset_factory(
        Event,
        fields=('name', 'event_date'),
        extra=0
    )
    qry = Event.events.all().order_by('event_date')
    pg = Paginator(qry, 4)
    page = request.GET.get('page')
    try:
        event_records = pg.page(page)
    except PageNotAnInteger:
        event_records = pg.page(1)
    except EmptyPage:
        event_records = pg.page(pg.num_pages)
    if request.method == 'POST':
        formset = EventsFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return_url = '/allevents/'
            if 'page' in request.GET:
                return_url += '?page=' + request.GET['page']
            return HttpResponseRedirect(return_url)
    else:
        page_qry = qry.filter(id__in=[event.id for event in event_records])
        formset = EventsFormSet(queryset=page_qry)

    context = {'event_records': event_records, 'formset': formset}
    messages.debug(request, qry)
    return render(request, 'events/all_events.html', context)


def list_subscribers(request):
    p = Paginator(MyClubUser.objects.all(), 3)
    page = request.GET.get('page')
    subcribers = p.get_page(page)
    return render(request, 'events/subscribers.html', {'subscribers': subcribers})


class Event_view(TemplateView):

    template_name = 'events/event_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'MyClub_Events'
        return context


class MyClubListView(ListView):
    model = Event
    context_object_name = 'all_events'


class MyClubDetailView(DetailView):
    model = Event
    context_object_name = 'event'


class MyClubCreateEvent(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Event
    success_url = reverse_lazy('show-events')
    form_class = EventForm


class MyClubUpdateEvent(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Event
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('show-events')
    form_class = EventForm


class MyClubDeleteEvent(DeleteView):
    model = Event
    context_object_name = 'event'
    success_url = reverse_lazy('show-events')


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)