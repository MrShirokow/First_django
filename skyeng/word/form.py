from django import forms
from .model import Word


class WordForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['theme', 'name', 'transcription', 'translation', 'example', 'sound']
