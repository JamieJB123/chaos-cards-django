from django import forms
from .models import CollaborateRequest


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={
                'maxlength': '200',
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message'
            })
        }
