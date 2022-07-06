from django import forms
from .model import Theme


class ThemeForm(forms.ModelForm):

    category_id = forms.IntegerField()

    class Meta:
        model = Theme
        fields = ['level', 'name', 'photo']
