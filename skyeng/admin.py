import csv
from django.contrib import admin
from skyeng.models import Category, Theme, Word


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_preview')
    readonly_fields = ('icon_preview',)
    list_display_links = ('id', 'name')

    def export_to_csv(self, request, queryset):
        with open('data.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name'])
            for category in queryset:
                writer.writerow([category.id, category.name])

    def icon_preview(self, item):
        return item.icon_preview

    icon_preview.short_description = 'icon preview'
    icon_preview.allow_tags = True


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'category', 'photo_preview')
    readonly_fields = ('photo_preview',)
    list_display_links = ('id', 'name')

    def photo_preview(self, item):
        return item.photo_preview

    photo_preview.short_description = 'photo preview'
    photo_preview.allow_tags = True


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'transcription', 'translation', 'example', 'sound_display')
    readonly_fields = ('sound_display',)
    list_display_links = ('id', 'name')

    def sound_display(self, item):
        return item.sound_display

    sound_display.short_description = 'sound'
    sound_display.allow_tags = True
