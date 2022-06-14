from django.db import models
from skyeng.theme.model import Theme
from django.utils.html import mark_safe


class Word(models.Model):
    theme = models.ManyToManyField(Theme, related_name='words')
    name = models.CharField(max_length=200, null=True, blank=True)
    transcription = models.CharField(max_length=200, null=True, blank=True)
    translation = models.CharField(max_length=200, null=True, blank=True)
    example = models.TextField(null=True, blank=True)
    sound = models.FileField(upload_to='sounds/', blank=True)

    @property
    def sound_display(self):
        if self.sound:
            return mark_safe(f'<audio controls name="media"><source src="{self.sound.url}" type="audio/mpeg"></audio>')
        return ""

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
        ordering = ['id']
