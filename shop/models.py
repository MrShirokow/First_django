from django.db import models
from datetime import date
from enum import Enum


class AnimalType(Enum):
    CAT = 'Cat'
    DOG = 'Dog'


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    animal = models.CharField(max_length=20, choices=[(type.name, type.value) for type in AnimalType])
    birthday = models.DateField()

    @property
    def age(self):
        return int((date.today() - self.birthday).days // 365.2425)

    def __str__(self):
        return f'{self.animal}, name: {self.name}, age: {self.age} years'
