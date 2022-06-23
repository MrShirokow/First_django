from django.views import View
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponse
from .category.form import CategoryForm
from .category.model import Category
from .theme.model import Theme, Level
from .theme.form import ThemeForm
from .word.model import Word
from .word.form import WordForm
from .serializers import serialize_category_list, serialize_level, serialize_word, serialize_theme, \
    serialize_theme_list, serialize_word_list
from first_app.settings import API_SECRET


def api_secret_check(request_function):
    def request_wrapper(self, request, *args, **kwargs):
        secret = request.headers.get('SECRET')
        if API_SECRET != secret:
            return HttpResponseForbidden('Unknown API key')
        return request_function(self, request, *args, **kwargs)

    return request_wrapper


def paginate(query_params, query_set):
    count = query_set.count()
    offset = int(query_params.get('offset', 0))
    limit = int(query_params.get('limit', 50))
    if limit > 100 or limit < 0 or offset < 0 or offset > count:
        return None
    return query_set[offset:offset + limit]


class CategoryListView(View):

    @api_secret_check
    def get(self, request):
        query_set = Category.objects.all()
        query_params = request.GET
        query_set = paginate(query_params, query_set)
        if query_set is None:
            return HttpResponse('Invalid limit or offset value', status=422)

        items_data = serialize_category_list(request, query_set)
        return JsonResponse(items_data, safe=False)

    @api_secret_check
    def post(self, request):
        request_body = request.POST
        request_files = request.FILES
        category_form = CategoryForm(request_body, request_files)
        if category_form.is_valid():
            name = request_body.get('name')
            icon = request_files.get('icon')
            Category.objects.create(name=name, icon=icon)

        return HttpResponse('Creation was successful', status=201)


class ThemeListView(View):

    @api_secret_check
    def get(self, request):
        query_params = request.GET
        query_set = Theme.objects.all()
        category_id = query_params.get('category')
        level = query_params.get('level')
        if category_id:
            query_set = query_set.filter(category=category_id)
        if level:
            query_set = query_set.filter(level=level)

        query_set = paginate(query_params, query_set)
        if query_set is None:
            return HttpResponse('Invalid limit or offset value', status=422)

        items_data = serialize_theme_list(request, query_set)
        return JsonResponse(items_data, safe=False)

    @api_secret_check
    def post(self, request):
        request_body = request.POST
        request_files = request.FILES
        theme_form = ThemeForm(request_body, request_files)
        if theme_form.is_valid():
            pass

        return HttpResponse('Success', status=201)


class ThemeDetailView(View):

    @api_secret_check
    def get(self, request, theme_id):
        theme = Theme.objects.filter(id=theme_id).first()
        if not theme:
            return HttpResponseNotFound(f'Theme with id={theme_id} not found')

        words = theme.words.all()
        item_data = serialize_theme(request, theme, words)
        return JsonResponse(item_data, safe=False)


class LevelDetailView(View):

    @api_secret_check
    def get(self, request):
        items_data = serialize_level(Level)
        return JsonResponse(items_data, safe=False)


class WordDetailView(View):

    @api_secret_check
    def get(self, request, word_id):
        word = Word.objects.filter(id=word_id).first()
        if not word:
            return HttpResponseNotFound(f'Word with id={word_id} not found')

        item_data = serialize_word(request, word)
        return JsonResponse(item_data)


class WordListView(View):

    @api_secret_check
    def get(self, request):
        query_set = Word.objects.all()
        query_params = request.GET
        query_set = paginate(query_params, query_set)
        if query_set is None:
            return HttpResponse('Invalid limit or offset value', status=422)

        items_data = serialize_word_list(query_set)
        return JsonResponse(items_data, safe=False)

    @api_secret_check
    def post(self, request):
        request_body = request.POST
        request_files = request.FILES
        word_form = WordForm(request_body, request_files)
        if word_form.is_valid():
            pass

        return HttpResponse('Success', status=201)
