from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Genre(models.Model):
    """Класс жанров фильмов."""

    title = models.CharField('Жанр', max_length=100)


class Type(models.Model):
    """Класс типа (фильм, мульт, сериал)."""

    title = models.CharField('Тип', max_length=100)


class Country(models.Model):
    """Страна производитель фильма."""

    title = models.CharField('Страна', max_length=255)


class Director(models.Model):
    """Режиссер фильма."""

    name = models.CharField('Имя', max_length=255)


class Film(models.Model):
    """Основная абстракция приложения - фильм."""

    title = models.CharField('Название', max_length=255)
    rating = models.DecimalField('Оценка', max_digits=2, decimal_places=1)
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name='Тип',
        help_text='Например: фильм, мультфильм, сериал.'   
    )
    