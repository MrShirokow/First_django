from django.forms import ModelForm
from model import Word


class CategoryForm(ModelForm):

    class Meta:
        model = Word
        fields = ['theme', 'name', 'transcription', 'translation', 'example', 'sound']
