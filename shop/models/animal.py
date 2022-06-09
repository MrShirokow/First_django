from django.db import models
from datetime import datetime


class Animal(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField()

    @property
    def age(self):
        return (datetime.now() - self.birthday).year

    def __str__(self):
        return f'{self.name} {self.age}'
