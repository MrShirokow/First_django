import json

import skyeng.internal.serializers as serializers
import skyeng.internal.utils as utils

from django.db import connection
from django.views import View
from django.core.files import File
from django.core.files.images import ImageFile
from skyeng.internal.models.category.form import CategoryForm
from skyeng.internal.models.category.model import Category
from skyeng.internal.models.theme.model import Theme, Level
from skyeng.internal.models.theme.form import ThemeForm
from skyeng.internal.models.word.model import Word
from skyeng.internal.models.word.form import WordForm
from django.http import HttpRequest, JsonResponse, HttpResponseNotFound, HttpResponse


class CategoryListView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        query_set = Category.objects.all()
        query_params = request.GET
        query_set = serializers.serialize_category_list(request, utils.paginate(query_params, query_set))
        return JsonResponse(query_set, safe=False)

    def post(self, request: HttpRequest) -> HttpResponse:
        request_body = json.loads(request.body)
        file_content = utils.decode_file(request_body.get('icon'))
        request_files = {'icon': ImageFile(file_content, name='icon.jpg')}
        category_form = CategoryForm(request_body, request_files)

        if not category_form.is_valid():
            return HttpResponse('Creation is failed', status=400)

        Category.objects.create(name=request_body.get('name'),
                                icon=request_files.get('icon'))
        return HttpResponse('Creation is successful', status=201)


class ThemeListView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        query_params = request.GET
        query_set = Theme.objects.all()
        category_id = query_params.get('category')
        level = query_params.get('level')
        if category_id:
            query_set = query_set.filter(category_id=category_id)
        if level:
            query_set = query_set.filter(level=level)

        query_set = serializers.serialize_theme_list(request, utils.paginate(query_params, query_set))
        return JsonResponse(query_set, safe=False)

    def post(self, request: HttpRequest) -> HttpResponse:
        request_body = json.loads(request.body)
        file_content = utils.decode_file(request_body.get('photo'))
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

    def get(self, request: HttpRequest, theme_id: int) -> JsonResponse | HttpResponseNotFound:
        theme = Theme.objects.filter(pk=theme_id).select_related('category').prefetch_related('words').first()
        if not theme:
            return HttpResponseNotFound(f'Theme with id={theme_id} not found')

        words = theme.words.all()
        item_data = serializers.serialize_theme(request, theme, words)
        return JsonResponse(item_data, safe=False)


class LevelDetailView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        items_data = serializers.serialize_level(Level)
        return JsonResponse(items_data, safe=False)


class WordDetailView(View):

    def get(self, request: HttpRequest, word_id: int) -> JsonResponse | HttpResponseNotFound:
        word = Word.objects.filter(id=word_id).first()
        if not word:
            return HttpResponseNotFound(f'Word with id={word_id} not found')

        item_data = serializers.serialize_word(request, word)
        return JsonResponse(item_data)


class WordListView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        query_set = Word.objects.all()
        query_params = request.GET
        query_set = serializers.serialize_word_list(utils.paginate(query_params, query_set))
        return JsonResponse(query_set, safe=False)

    def post(self, request: HttpRequest) -> HttpResponse:
        request_body = json.loads(request.body)
        file_content = utils.decode_file(request_body.get('sound'))
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
