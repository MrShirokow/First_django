from django.forms import ModelForm, ModelChoiceField
from .model import Word


class WordForm(ModelForm):

    # theme = ModelChoiceField(queryset=Word.objects.all())

    class Meta:
        model = Word
        fields = ['theme', 'name', 'transcription', 'translation', 'example', 'sound']
