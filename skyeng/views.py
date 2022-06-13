from django.views import View
from django.http import JsonResponse
from .category.model import Category
from .theme.model import Theme, Level
from .word.model import Word


class ThemeView(View):

    def get(self, request):
        query = request.GET
        category_id = query.get('category')
        level = query.get('level')
        qs = Theme.objects.all()
        if category_id:
            qs = qs.filter(category=category_id)
        if level:
            qs = qs.filter(level=level)

        items_data = [{
                'id': item.id,
                'category': item.category.id,
                'level': item.level,
                'name': item.name} for item in qs]

        return JsonResponse(items_data, safe=False)


class ThemeByIdView(View):
    def get(self, request, **kwargs):
        theme_id = kwargs.get('theme_id')
        item = Theme.objects.get(id=theme_id)
        words = Word.objects.filter(theme=theme_id)
        item_data = {
            'id': item.id,
            'category': item.category.id,
            'level': item.level,
            'name': item.name,
            'words': [{'id': w.id,
                       'word': w.name} for w in words]
        }

        return JsonResponse(item_data, safe=False)


class LevelView(View):

    def get(self, request):
        items_data = [{
                'name': item.value,
                'code': item.name} for item in Level]

        return JsonResponse(items_data, safe=False)


class CategoryView(View):

    def get(self, request):
        qs = Category.objects.all()
        items_data = [{
                'id': item.id,
                'name': item.name} for item in qs]

        return JsonResponse(items_data, safe=False)


class WordView(View):

    def get(self, request, **kwargs):
        word_id = kwargs.get('word_id')
        item = Word.objects.get(id=word_id)
        item_data = {
            'id': item.id,
            'name': item.name,
            'transcription': item.transcription,
            'translation': item.translation,
            'example': item.example,
        }

        return JsonResponse(item_data)
