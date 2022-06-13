from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    icon = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
