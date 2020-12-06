from django.db.models import Model
from django.forms import ModelForm
from django import forms
from events.models import Venue


class VenueForm(ModelForm):
    requires_css_class = 'required'

    class Meta:
        model = Venue
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        email_address = cleaned_data.get("email_address")
        if not(phone or email_address):
            raise forms.ValidationError(
                "You must enter either a phone number or an email, both."
            )

