from django.db import models
from datetime import date


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    CAT = 'CT'
    DOG = 'DG'
    ANIMALS = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
    ]
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    animal = models.CharField(max_length=30, choices=ANIMALS, default=DOG)
    birthday = models.DateField()

    @property
    def age(self):
        return int((date.today() - self.birthday).days // 365.2425)

    def __str__(self):
        return f'{self.animal} name: {self.name}, age: {self.age} years'
