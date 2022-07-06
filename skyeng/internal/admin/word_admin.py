from django.contrib import admin
from skyeng.models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'transcription', 'translation', 'example', 'sound_display')
    readonly_fields = ('sound_display',)
    list_display_links = ('id', 'name')

    def sound_display(self, item):
        return item.sound_display

    sound_display.short_description = 'sound'
    sound_display.allow_tags = True
