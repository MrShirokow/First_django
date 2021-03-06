from django.db import models
from django.utils.html import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    icon = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def icon_preview(self):
        if self.icon:
            return mark_safe(f'<img src="{self.icon.url}" width="50" height="50" />')
        return ""

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
