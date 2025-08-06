from django import forms
from .models import CollaborateRequest


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message',)
