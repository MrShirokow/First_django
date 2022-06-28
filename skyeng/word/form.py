from django import forms
from .model import Word


class WordForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['name', 'transcription', 'translation', 'example', 'sound']
