"""
Model's serializers
"""


def serialize_category_list(request, query_set):
    return [{
        'id': item.id,
        'name': item.name,
        'icon': request.build_absolute_uri(item.icon.url)} for item in query_set
    ]


def serialize_level(levels):
    return [{
        'name': item.value,
        'code': item.name} for item in levels
    ]


def serialize_word(request, word):
    return {
        'id': word.id,
        'name': word.name,
        'transcription': word.transcription,
        'translation': word.translation,
        'example': word.example,
        'sound': request.build_absolute_uri(word.sound.url)
    }


def serialize_word_list(query_set):
    return [{
        'id': word.id,
        'name': word.name} for word in query_set
    ]


def serialize_theme(request, theme_item, words):
    return {
        'id': theme_item.id,
        'category': theme_item.category.id,
        'level': theme_item.level,
        'name': theme_item.name,
        'photo': request.build_absolute_uri(theme_item.photo.url),
        'words': serialize_word_list(words)
    }


def serialize_theme_list(request, query_set):
    return [{
        'id': item.id,
        'category': item.category.id,
        'level': item.level,
        'name': item.name,
        'photo': request.build_absolute_uri(item.photo.url)} for item in query_set
    ]
