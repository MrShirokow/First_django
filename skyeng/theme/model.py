from django.db import models
from enum import Enum
from skyeng.category.model import Category
from django.utils.html import mark_safe


class Level(Enum):
    A1 = 'Beginner'
    A2 = 'Elementary'
    B1 = 'Intermediate'
    B2 = 'Upper-Intermediate'
    C1 = 'Advanced'
    C2 = 'Proficiency'


class Theme(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='themes')
    level = models.CharField(max_length=30, choices=[(lev.name, lev.value) for lev in Level], null=True)
    name = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to='images/', null=True)

    @property
    def photo_preview(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="50" height="50" />')
        return ""

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'
        ordering = ['id']
