from django.db import models
from datetime import date


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Animal(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField()

    @property
    def age(self):
        return int((date.today() - self.birthday).days // 365.2425)


    def __str__(self):
        return f'name: {self.name}, age: {self.age}'
