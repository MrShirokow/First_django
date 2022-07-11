import base64
import functools
import hashlib
import hmac
import json
import io

import skyeng.internal.serializers as serializers

from django.db import connection
from django.core.files import File
from django.core.files.images import ImageFile
from django.views import View
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from skyeng.internal.models.category.form import CategoryForm
from skyeng.internal.models.category.model import Category
from skyeng.internal.models.theme.model import Theme, Level
from skyeng.internal.models.theme.form import ThemeForm
from skyeng.internal.models.word.model import Word
from skyeng.internal.models.word.form import WordForm


def api_secret_check(request_function):

    @functools.wraps(request_function)
    def request_wrapper(self, request, *args, **kwargs):
        # if request.headers.get('X-Signature') != get_signature(request, API_SECRET):
        #     return HttpResponseForbidden('Unknown API key')
        return request_function(self, request, *args, **kwargs)

    return request_wrapper


def get_signature(request, key):
    request_str = f'{request.method}\n{request.path}'
    return hmac.new(key.encode(), request_str.encode(), hashlib.sha256).hexdigest()


def positive_int(integer_string, strict=False, cutoff=None):
    number = int(integer_string)
    if number < 0 or (number == 0 and strict):
        raise ValueError()
    if cutoff:
        return min(number, cutoff)
    return number


def get_limit(query_params, default=50):
    try:
        return positive_int(query_params.get('limit'),
                            strict=True,
                            cutoff=100)
    except (TypeError, ValueError):
        return default


def get_offset(query_params):
    try:
        return positive_int(query_params.get('offset'))
    except (TypeError, ValueError):
        return 0


def paginate(query_params, query_set):
    offset = get_offset(query_params)
    limit = get_limit(query_params)
    return query_set[offset:offset + limit]


def decode_file(encoded_data: str):
    return io.BytesIO(base64.b64decode(encoded_data.encode('utf-8')))


class CategoryListView(View):

    @api_secret_check
    def get(self, request):
        query_set = Category.objects.all()
        query_params = request.GET
        query_set = serializers.serialize_category_list(request, paginate(query_params, query_set))
        return JsonResponse(query_set, safe=False)

    @api_secret_check
    def post(self, request):
        request_body = json.loads(request.body)
        file_content = decode_file(request_body.get('icon'))
        request_files = {'icon': ImageFile(file_content, name='icon.jpg')}
        category_form = CategoryForm(request_body, request_files)

        if not category_form.is_valid():
            return HttpResponse('Creation is failed', status=400)

        Category.objects.create(name=request_body.get('name'),
                                icon=request_files.get('icon'))
        return HttpResponse('Creation is successful', status=201)


class ThemeListView(View):

    @api_secret_check
    def get(self, request):
        query_params = request.GET
        query_set = Theme.objects.all()
        category_id = query_params.get('category')
        level = query_params.get('level')
        if category_id:
            query_set = query_set.filter(category_id=category_id)
        if level:
            query_set = query_set.filter(level=level)

        query_set = serializers.serialize_theme_list(request, paginate(query_params, query_set))
        return JsonResponse(query_set, safe=False)

    @api_secret_check
    def post(self, request):
        request_body = json.loads(request.body)
        file_content = decode_file(request_body.get('photo'))
        request_files = {'photo': ImageFile(file_content, name='photo.jpg')}

        theme_form = ThemeForm(request_body, request_files)
        if not theme_form.is_valid():
            return HttpResponse('Creation is failed', status=400)

        category_id = request_body.get('category_id')
        if not Category.objects.filter(pk=category_id).first():
            return HttpResponseNotFound(f'Category with id={category_id} not found')

        Theme.objects.create(category_id=category_id,
                             name=request_body.get('name'),
                             level=request_body.get('level'),
                             photo=request_files.get('photo'))
        return HttpResponse('Creation is successful', status=201)


class ThemeDetailView(View):

    @api_secret_check
    def get(self, request, theme_id):
        theme = Theme.objects.filter(pk=theme_id).select_related('category').prefetch_related('words').first()
        if not theme:
            return HttpResponseNotFound(f'Theme with id={theme_id} not found')

        words = theme.words.all()
        item_data = serializers.serialize_theme(request, theme, words)
        return JsonResponse(item_data, safe=False)


class LevelDetailView(View):

    @api_secret_check
    def get(self, request):
        items_data = serializers.serialize_level(Level)
        return JsonResponse(items_data, safe=False)


class WordDetailView(View):

    @api_secret_check
    def get(self, request, word_id):
        word = Word.objects.filter(id=word_id).first()
        if not word:
            return HttpResponseNotFound(f'Word with id={word_id} not found')

        item_data = serializers.serialize_word(request, word)
        return JsonResponse(item_data)


class WordListView(View):

    @api_secret_check
    def get(self, request):
        query_set = Word.objects.all()
        query_params = request.GET
        query_set = serializers.serialize_word_list(paginate(query_params, query_set))
        return JsonResponse(query_set, safe=False)

    @api_secret_check
    def post(self, request):
        request_body = json.loads(request.body)
        file_content = decode_file(request_body.get('sound'))
        request_files = {'sound': File(file_content, name='sound.mp3')}
        word_form = WordForm(request_body, request_files)
        if not word_form.is_valid():
            return HttpResponse('Creation is failed', status=400)

        request_ids = [theme_id.get('id') for theme_id in request_body.get('themes')]
        themes = Theme.objects.filter(id__in=request_ids)

        if not themes:
            return HttpResponseNotFound('Themes with such ids not found')

        new_word = Word.objects.create(name=request_body.get('name'),
                                       transcription=request_body.get('transcription'),
                                       translation=request_body.get('translation'),
                                       example=request_body.get('example'),
                                       sound=request_files.get('sound'))
        new_word.themes.add(*themes)

        return HttpResponse('Creation is successful', status=201)
