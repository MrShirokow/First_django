from django import forms
from .model import Theme


class ThemeForm(forms.ModelForm):

    category = forms.IntegerField()

    class Meta:
        model = Theme
        fields = ['level', 'name', 'photo']
