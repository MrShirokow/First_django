from django.views import View
from django.http import JsonResponse
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word
import json


class ThemeView(View):

    def get(self, request):
        qs = Theme.objects.all()
        items_data = []

        for item in qs:
            items_data.append({
                'id': item.id,
                'category': item.category.id,
                'level': item.level,
                'name': item.title,
            })
        data = {
            'items': items_data,
        }
        return JsonResponse(data)


class LevelView(View):

    def get(self, request):
        items_data = []

        for item in Level:
            items_data.append({
                'name': item.value,
                'code': item.name,
            })
        data = {
            'items': items_data,
        }
        return JsonResponse(data)


class CategoryView(View):

    def get(self, request):
        qs = Category.objects.all()
        items_data = []

        for item in qs:
            items_data.append({
                'id': item.id,
                'name': item.title,
            })
        data = {
            'items': items_data,
        }
        return JsonResponse(data)


class WordView(View):

    def get(self, request):
        pass
