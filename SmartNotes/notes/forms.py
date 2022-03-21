from django.core.exceptions import ValidationError

from .models import Note
from django import forms


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text"]
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})

        }
        labels = {
            'text': 'Write your thoughts here:'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if ";" in title:
            raise ValidationError("Invalid character in title. Please write a different title")
        return title
