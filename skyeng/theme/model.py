from django.db import models
from enum import Enum
from skyeng.category.model import Category


class Level(Enum):
    A1 = 'Beginner'
    A2 = 'Elementary'
    B1 = 'Intermediate'
    B2 = 'Upper-Intermediate'
    C1 = 'Advanced'
    C2 = 'Proficiency'


class Theme(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField(max_length=30, choices=[(lev.name, lev.value) for lev in Level], blank=True, null=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'Theme: {self.title}'

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'
