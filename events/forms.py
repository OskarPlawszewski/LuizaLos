from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    #  FIXME export to other app
    class Meta:
        model = Event
        fields = ('title', 'text',)