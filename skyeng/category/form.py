from django.forms import ModelForm
from model import Category


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'icon']
