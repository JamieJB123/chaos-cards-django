from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'content', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

