from django.contrib.auth import get_user_model
from django.db.models import F


def update_word_count():
    """
    Function update field 'word_counter' for all users
    """
    users = get_user_model().objects.all()
    users.update(word_counter=F('word_counter') + 10)
