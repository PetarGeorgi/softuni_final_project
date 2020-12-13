from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import AdminSite
from . models import Venue, MyClubUser, Event


class EventsAdmin(AdminSite):
    site_header = "MyClub Events Administration"
    site_title = "MyClub Events Admin"
    index_title = "MyClub events Admin Home"


admin_site = EventsAdmin(name="eventsadmin")


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('Required Information', {
            'description': 'These fields are required for each event.',
            'fields': (('name', 'venue'), 'event_date')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('description', 'manager')
        }),
    )


admin.site.register(MyClubUser)

