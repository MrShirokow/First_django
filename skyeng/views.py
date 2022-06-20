from django.views import View
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponse
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word
from .serializers import serialize_category_list, serialize_level, serialize_word, serialize_theme, serialize_theme_list
from first_app.settings import API_SECRET


def check_correct_api_secret(request):
    secret = request.headers.get('SECRET')
    return API_SECRET == secret


def paginate(query_params, query_set):
    offset = int(query_params.get('offset', 0))
    limit = int(query_params.get('limit', 50))

    return query_set[offset:limit]


class CategoryListView(View):

    def get(self, request):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        query_set = Category.objects.all()
        query_params = request.GET
        query_set = paginate(query_params, query_set)
        items_data = serialize_category_list(request, query_set)
        return JsonResponse(items_data, safe=False)


class ThemeListView(View):

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

        query_set = paginate(query_params, query_set)
        items_data = serialize_theme_list(request, query_set)
        return JsonResponse(items_data, safe=False)


class ThemeDetailView(View):

    def get(self, request, theme_id):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        theme = Theme.objects.filter(id=theme_id).first()
        if not theme:
            return HttpResponseNotFound(f'Theme with id {theme_id} not found')

        words = theme.words.all()
        item_data = serialize_theme(request, theme, words)
        return JsonResponse(item_data, safe=False)


class LevelDetailView(View):

    def get(self, request):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        items_data = serialize_level(Level)
        return JsonResponse(items_data, safe=False)


class WordDetailView(View):

    def get(self, request, word_id):
        if not check_correct_api_secret(request):
            return HttpResponseForbidden('Unknown API key')

        word = Word.objects.filter(id=word_id).first()
        if not word:
            return HttpResponseNotFound(f'Word with id {word_id} not found')

        item_data = serialize_word(request, word)
        return JsonResponse(item_data)
