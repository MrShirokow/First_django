from django.contrib import admin
from skyeng.models import Category, Theme, Word


class CategoryAdmin(admin.ModelAdmin):
    pass


class ThemeAdmin(admin.ModelAdmin):
    pass


class WordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Word, WordAdmin)

