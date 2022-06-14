from django.contrib import admin
from skyeng.models import Category, Theme, Word


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'icon_preview')
    readonly_fields = ('icon_preview',)
    list_display_links = ('id', 'name')

    def icon_preview(self, item):
        return item.icon_preview

    icon_preview.short_description = 'Icon preview'
    icon_preview.allow_tags = True


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'category', 'photo', 'photo_preview')
    readonly_fields = ('photo_preview',)
    list_display_links = ('id', 'name')

    def photo_preview(self, item):
        return item.photo_preview

    photo_preview.short_description = 'Photo preview'
    photo_preview.allow_tags = True


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'transcription', 'translation', 'example')
    list_display_links = ('id', 'name')
