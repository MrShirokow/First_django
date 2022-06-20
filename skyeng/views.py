from django.views import View
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word
from .serializers import serialize_category, serialize_level, serialize_word, serialize_theme, serialize_theme_list
from first_app.settings import API_SECRET


def check_correct_api_secret(request):
    secret = request.META.get('HTTP_SECRET')
    return API_SECRET == secret


def get_offset_and_limit(query_params, items_count):
    offset = query_params.get('offset')
    limit = query_params.get('limit')
    offset = int(offset) if offset else 0
    limit = int(limit) + offset if limit else items_count

    return offset, limit


class CategoryView(View):

    def get(self, request):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        query_params = request.GET
        items_count = Category.objects.count()
        offset, limit = get_offset_and_limit(query_params, items_count)
        query_set = Category.objects.all()[offset:limit]

        items_data = serialize_category(request, query_set)
        return JsonResponse(items_data, safe=False)


class ListThemeView(View):

    def get(self, request):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        query_params = request.GET
        query_set = Theme.objects.all()
        category_id = query_params.get('category')
        level = query_params.get('level')
        if category_id:
            query_set = query_set.filter(category=category_id)
        if level:
            query_set = query_set.filter(level=level)

        items_count = query_set.count()
        offset, limit = get_offset_and_limit(query_params, items_count)
        query_set = query_set[offset:limit]

        items_data = serialize_theme_list(request, query_set)
        return JsonResponse(items_data, safe=False)


class ThemeView(View):

    def get(self, request, theme_id):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        theme = Theme.objects.filter(id=theme_id).first()
        if not theme:
            return HttpResponseNotFound(f'Theme with id {theme_id} not found')

        words = theme.words.all()
        item_data = serialize_theme(request, theme, words)
        return JsonResponse(item_data, safe=False)


class LevelView(View):

    def get(self, request):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        items_data = serialize_level(Level)
        return JsonResponse(items_data, safe=False)


class WordView(View):

    def get(self, request, word_id):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        word = Word.objects.filter(id=word_id).first()
        if not word:
            return HttpResponseNotFound(f'Word with id {word_id} not found')

        item_data = serialize_word(request, word)
        return JsonResponse(item_data)
