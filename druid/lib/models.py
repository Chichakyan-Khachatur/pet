from django.db import models

class Texts(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    link = models.CharField(max_length=50, verbose_name='Путь')

    class Meta:
        verbose_name_plural = 'Тексты'
        verbose_name = 'Текст'
