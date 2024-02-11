from django.db import models

class Cards(models.Model):
    tipes = (
        (1, 'один вариант'),
        (2, 'много вариантов'),
        (3, 'один из многих'),
        (4, 'много из многих')
    )
    question = models.CharField(max_length=100, verbose_name='вопрос')
    options = models.JSONField(verbose_name='Список вариантов')
    answers = models.JSONField(verbose_name='список ответов')
    tipe = models.SmallIntegerField(choices=tipes, default=1, verbose_name='тип карточки')

    class Meta:
        verbose_name_plural = 'Карточки'
        verbose_name ='Карточка'

class Libraries(models.Model):
    name = models.CharField(max_length=100, verbose_name='назание')
    discription = models.TextField(max_length=300, verbose_name='Описание')
    cards = models.ManyToManyField(Cards, verbose_name='карточки')

    class Meta:
        verbose_name_plural = 'Библиотеки'
        verbose_name ='Библиотека'


