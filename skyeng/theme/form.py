from django.forms import ModelForm
from .model import Theme


class ThemeForm(ModelForm):

    class Meta:
        model = Theme
        fields = ['level', 'name', 'photo']
