"""
Model's serializers
"""


def serialize_category(request, query_set):
    items_data = [{
        'id': item.id,
        'name': item.name,
        'icon': request.build_absolute_uri(item.icon.url)} for item in query_set
    ]
    return items_data


def serialize_level(levels):

    items_data = [{
        'name': item.value,
        'code': item.name} for item in levels
    ]
    return items_data


def serialize_word(request, word):
    item_data = {
        'id': word.id,
        'name': word.name,
        'transcription': word.transcription,
        'translation': word.translation,
        'example': word.example,
        'sound': request.build_absolute_uri(word.sound.url)
    }
    return item_data


def serialize_theme(request, theme_item, theme_words):
    item_data = {
        'id': theme_item.id,
        'category': theme_item.category.id,
        'level': theme_item.level,
        'name': theme_item.name,
        'photo': request.build_absolute_uri(theme_item.photo.url),
        'words': [{'id': w.id,
                   'word': w.name} for w in theme_words]
    }
    return item_data


def serialize_theme_list(request, query_set):
    items_data = [{
        'id': item.id,
        'category': item.category.id,
        'level': item.level,
        'name': item.name,
        'photo': request.build_absolute_uri(item.photo.url)} for item in query_set
    ]
    return items_data
