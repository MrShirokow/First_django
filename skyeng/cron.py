import os
import django

from django.db.models import F
from django.conf import settings
from django.contrib.auth import get_user_model


def update_word_count():
    """
    Function update field 'word_counter' for all users
    """
    users = get_user_model().objects.all()
    users.update(word_counter=F('word_counter') + 10)


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    if not settings.configured:
        django.setup()
    update_word_count()
