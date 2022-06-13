from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    icon = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'category: {self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
