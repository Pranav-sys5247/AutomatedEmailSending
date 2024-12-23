from django import forms
from .models import birthday

class birthday(forms.ModelForm):
    class Meta:
        model = birthday
        fields = ['sender_email', 'receiver_email', 'message', 'date', 'image']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
