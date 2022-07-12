from django.contrib.auth import models


class User(models.AbstractUser):
    pass

    def __str__(self):
        return self.username
