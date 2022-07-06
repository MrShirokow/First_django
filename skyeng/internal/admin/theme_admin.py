from django.contrib import admin
from skyeng.models import Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'category', 'photo_preview')
    readonly_fields = ('photo_preview',)
    list_display_links = ('id', 'name')

    def photo_preview(self, item):
        return item.photo_preview

    photo_preview.short_description = 'photo preview'
    photo_preview.allow_tags = True
