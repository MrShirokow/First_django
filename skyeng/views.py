from django.views import View
from django.http import JsonResponse
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word
from django.http import HttpResponseNotFound
from .serializers import *


class ListThemeView(View):

    def get(self, request):

        query = request.GET
        category_id = query.get('category')
        level = query.get('level')
        query_set = Theme.objects.all()
        if category_id:
            query_set = query_set.filter(category=category_id)
        if level:
            query_set = query_set.filter(level=level)

        items_data = serialize_theme_list(request, query_set)
        return JsonResponse(items_data, safe=False)


class ThemeView(View):

    def get(self, request, theme_id):
        theme = Theme.objects.filter(id=theme_id).first()
        if not theme:
            return HttpResponseNotFound('Not found')

        words = theme.words.all()
        item_data = serialize_theme(request, theme, words)
        return JsonResponse(item_data, safe=False)


class LevelView(View):

    def get(self, request):
        items_data = serialize_level(Level)
        return JsonResponse(items_data, safe=False)


class CategoryView(View):

    def get(self, request):
        query_set = Category.objects.all()
        items_data = serialize_category(request, query_set)
        return JsonResponse(items_data, safe=False)


class WordView(View):

    def get(self, request, word_id):
        word = Word.objects.filter(id=word_id).first()
        if not word:
            return HttpResponseNotFound('Not found')

        item_data = serialize_word(request, word)
        return JsonResponse(item_data)
