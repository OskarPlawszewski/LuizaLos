from django import forms

from .models import Post
from .models import Event


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class EventForm(forms.ModelForm):
    #  FIXME export to other app
    class Meta:
        model = Event
        fields = ('title', 'text',)