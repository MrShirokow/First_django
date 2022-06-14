from django.db import models
from skyeng.theme.model import Theme


class Word(models.Model):
    theme = models.ManyToManyField(Theme, related_name='words')
    name = models.CharField(max_length=200, null=True, blank=True)
    transcription = models.CharField(max_length=200, null=True, blank=True)
    translation = models.CharField(max_length=200, null=True, blank=True)
    example = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'word: {self.name}'

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
        ordering = ['id']
