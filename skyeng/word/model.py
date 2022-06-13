from django.db import models
from skyeng.theme.model import Theme


class Word(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    # transcription = models.CharField(max_length=200)
    # translation = models.CharField(max_length=200)
    # example = models.TextField()

    def __str__(self):
        return f'{self.word}'

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
