from django.db import models

# Create your models here.
from django.urls import reverse


class Coloring_page(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя для раскраски')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='фото для раскраски')
    tema = models.ForeignKey('Tema', on_delete=models.CASCADE, verbose_name='тема раскраски')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'картинки для раскрасок'
        verbose_name_plural = 'картинки для раскрасок'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('Detail',kwargs={'page_slug':self.slug})


class Tema(models.Model):
    name = models.CharField(max_length=255, verbose_name='тема раскраски')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='контент для темы')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория для темы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тема для раскрасок'
        verbose_name_plural = 'тема для раскрасок'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('Tema', kwargs={'tema': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='категория для темы')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория раскрасок'
        verbose_name_plural = 'категория раскрасок'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('Category', kwargs={'category': self.slug})
