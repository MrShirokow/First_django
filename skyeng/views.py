from django.views import View
from django.http import JsonResponse
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word


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

        items_data = [{
                'id': item.id,
                'category': item.category.id,
                'level': item.level,
                'name': item.name,
                'photo': request.build_absolute_uri(item.photo.url)} for item in query_set
        ]

        return JsonResponse(items_data, safe=False)


class ThemeView(View):
    def get(self, request, **kwargs):
        theme_id = kwargs.get('theme_id')
        theme = Theme.objects.get(id=theme_id)
        words = theme.words.all()
        item_data = {
            'id': theme.id,
            'category': theme.category.id,
            'level': theme.level,
            'name': theme.name,
            'photo': request.build_absolute_uri(theme.photo.url),
            'words': [{'id': w.id,
                       'word': w.name} for w in words]
        }

        return JsonResponse(item_data, safe=False)


class LevelView(View):

    def get(self, request):
        items_data = [{
                'name': item.value,
                'code': item.name} for item in Level
        ]

        return JsonResponse(items_data, safe=False)


class CategoryView(View):

    def get(self, request):
        query_set = Category.objects.all()
        items_data = [{
                'id': item.id,
                'name': item.name,
                'icon': request.build_absolute_uri(item.icon.url)} for item in query_set
        ]

        return JsonResponse(items_data, safe=False)


class WordView(View):

    def get(self, request, **kwargs):
        word_id = kwargs.get('word_id')
        word = Word.objects.get(id=word_id)
        item_data = {
            'id': word.id,
            'name': word.name,
            'transcription': word.transcription,
            'translation': word.translation,
            'example': word.example,
        }

        return JsonResponse(item_data)
