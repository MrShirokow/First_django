from django.contrib import admin
from skyeng.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_preview')
    readonly_fields = ('icon_preview',)
    list_display_links = ('id', 'name')

    def icon_preview(self, item):
        return item.icon_preview

    icon_preview.short_description = 'icon preview'
    icon_preview.allow_tags = True
