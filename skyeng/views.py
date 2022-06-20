from django.views import View
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word
from .serializers import *
from first_app.settings import API_SECRET


class ListThemeView(View):

    def get(self, request):
        query_params = request.GET
        api_secret = query_params.get('api_secret')
        if API_SECRET != api_secret:
            return HttpResponseForbidden('Unknown API key')

        query_set = Theme.objects.all()
        category_id = query_params.get('category')
        level = query_params.get('level')
        if category_id:
            query_set = query_set.filter(category=category_id)
        if level:
            query_set = query_set.filter(level=level)

        offset = query_params.get('offset')
        limit = query_params.get('limit')
        item_count = Theme.objects.count()
        offset = int(offset if offset else 0)
        limit = int(limit) + offset if limit else item_count
        query_set = query_set[offset:limit]

        items_data = serialize_theme_list(request, query_set)
        return JsonResponse(items_data, safe=False)


class ThemeView(View):

    def get(self, request, theme_id):
        query_params = request.GET
        api_secret = query_params.get('api_secret')
        if API_SECRET != api_secret:
            return HttpResponseForbidden('Unknown API key')

        theme = Theme.objects.filter(id=theme_id).first()
        if not theme:
            return HttpResponseNotFound('Not found')

        words = theme.words.all()
        item_data = serialize_theme(request, theme, words)
        return JsonResponse(item_data, safe=False)


class LevelView(View):

    def get(self, request):
        query_params = request.GET
        api_secret = query_params.get('api_secret')
        if API_SECRET != api_secret:
            return HttpResponseForbidden('Unknown API key')

        items_data = serialize_level(Level)
        return JsonResponse(items_data, safe=False)


class CategoryView(View):

    def get(self, request):
        query_params = request.GET
        api_secret = query_params.get('api_secret')
        if API_SECRET != api_secret:
            return HttpResponseForbidden('Unknown API key')

        offset = query_params.get('offset')
        limit = query_params.get('limit')
        item_count = Category.objects.count()
        offset = int(offset if offset else 0)
        limit = int(limit) + offset if limit else item_count

        query_set = Category.objects.all()[offset:limit]
        items_data = serialize_category(request, query_set)
        return JsonResponse(items_data, safe=False)


class WordView(View):

    def get(self, request, word_id):
        query_params = request.GET
        api_secret = query_params.get('api_secret')
        if API_SECRET != api_secret:
            return HttpResponseForbidden('Unknown API key')

        word = Word.objects.filter(id=word_id).first()
        if not word:
            return HttpResponseNotFound('Not found')

        item_data = serialize_word(request, word)
        return JsonResponse(item_data)
