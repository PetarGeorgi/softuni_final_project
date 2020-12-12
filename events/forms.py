from django.db.models import Model
from django.forms import ModelForm, Textarea
from django import forms
from events.models import Venue, Event
from ckeditor.widgets import CKEditorWidget

# class VenueForm(ModelForm):
#     requires_css_class = 'required'
#
#     class Meta:
#         model = Venue
#         fields = '__all__'
#
#     def clean(self):
#         cleaned_data = super().clean()
#         phone = cleaned_data.get("phone")
#         email_address = cleaned_data.get("email_address")
#         if not(phone or email_address):
#             raise forms.ValidationError(
#                 "You must enter either a phone number or an email, both."
#             )


class MyFormWidget(forms.TextInput):
    class Media:
        css = {'all': ('widget.css',)}


class VenueForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Venue
        fields = '__all__'
        widgets = {
            'name': MyFormWidget(attrs={'class': 'mywidget'}),
            'address': Textarea(attrs={'cols': 40, 'rows': 3}),
            }
    """Override this clean() method to provide custom validation. """
    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        email_address = cleaned_data.get("email_address")
        if not (phone or email_address):
            raise forms.ValidationError(
             "You must enter either a phone number or an email,both."
              )

class EventForm(ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Event
        fields = ['name', 'event_date', 'description']