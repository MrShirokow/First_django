from django.views import View
from django.http import JsonResponse
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word
import json


class ThemeView(View):

    def get(self, request):
        qs = Theme.objects.all()
        items_data = [{
                'id': item.id,
                'category': item.category.id,
                'level': item.level,
                'name': item.title,} for item in qs]

        return JsonResponse(items_data, safe=False)


class LevelView(View):

    def get(self, request):
        items_data = [{
                'name': item.value,
                'code': item.name,} for item in Level]

        return JsonResponse(items_data, safe=False)


class CategoryView(View):

    def get(self, request):
        qs = Category.objects.all()
        items_data = [{
                'id': item.id,
                'name': item.title,} for item in qs]

        return JsonResponse(items_data, safe=False)


class WordView(View):

    def get(self, request):
        # Need change method to get word by id

        item = Word.objects.get(id=2)
        items_data = [{
            'id': item.id,
            'word': item.word,
            'transcription': item.transcription,
            'translation': item.translation,
            'example': item.example,
        }]

        return JsonResponse(items_data[0])
