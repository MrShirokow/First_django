from django.views import View
from django.http import JsonResponse
from models import Category, Theme, Word


# class ThemeView(View):
#
#     def get(self, request):
#         items_count = Theme.objects.count()
#         items = Theme.objects.all()
#
#         items_data = []
#         for item in items:
#             items_data.append({
#                 'category': item.category,
#                 'level': item.level,
#                 'title': item.title,
#             })
#
#         data = {
#             'items': items_data,
#             'count': items_count,
#         }
#
#         return JsonResponse(data)