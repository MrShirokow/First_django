from django import forms
from .model import Theme
from skyeng.category.model import Category


class ThemeForm(forms.ModelForm):

    class Meta:
        model = Theme
        fields = ['category', 'level', 'name', 'photo']
