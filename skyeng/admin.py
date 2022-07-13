from django.contrib import admin
from skyeng.models import Category, Theme, Word, User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ("id", "word_counter", "username", "email", "first_name", "last_name", "is_staff")
    list_display_links = ('id', 'username', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_preview')
    readonly_fields = ('icon_preview',)
    list_display_links = ('id', 'name')

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
