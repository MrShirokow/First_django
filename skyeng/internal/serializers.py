from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from skyeng.internal.models.theme.model import Level, Theme
from skyeng.internal.models.word.model import Word


def serialize_category_list(request: WSGIRequest, query_set: QuerySet) -> list:
    """
    The function serializes the category queryset and returns as a list
    """
    return [{
        'id': item.id,
        'name': item.name,
        'icon': request.build_absolute_uri(item.icon.url)} for item in query_set
    ]


def serialize_level(levels: Level) -> list:
    """
    The function serializes the levels and returns as a list
    """
    return [{
        'name': item.value,
        'code': item.name} for item in levels
    ]


def serialize_word(request: WSGIRequest, word: Word) -> dict:
    """
    The function serializes the 'Word' object and returns it as a dictionary of word's fields
    """
    return {
        'id': word.id,
        'name': word.name,
        'transcription': word.transcription,
        'translation': word.translation,
        'example': word.example,
        'sound': request.build_absolute_uri(word.sound.url)
    }


def serialize_word_list(query_set: QuerySet) -> list:
    """
    The function serializes the word queryset and returns as a list
    """
    return [{
        'id': word.id,
        'name': word.name} for word in query_set
    ]


def serialize_theme(request: WSGIRequest, theme_item: Theme, words: QuerySet) -> dict:
    """
    The function serializes the 'Theme' object and returns it as a dictionary of theme's fields
    """
    return {
        'id': theme_item.id,
        'category': theme_item.category.id,
        'level': theme_item.level,
        'name': theme_item.name,
        'photo': request.build_absolute_uri(theme_item.photo.url),
        'words': serialize_word_list(words)
    }


def serialize_theme_list(request: WSGIRequest, query_set: QuerySet) -> list:
    """
    The function serializes the theme queryset and returns as a list
    """
    return [{
        'id': item.id,
        'category': item.category.id,
        'level': item.level,
        'name': item.name,
        'photo': request.build_absolute_uri(item.photo.url)} for item in query_set
    ]
