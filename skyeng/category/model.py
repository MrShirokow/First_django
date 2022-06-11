from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
