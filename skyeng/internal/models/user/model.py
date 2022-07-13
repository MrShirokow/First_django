from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    word_counter = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.username
