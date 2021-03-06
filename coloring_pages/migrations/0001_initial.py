# Generated by Django 4.0.4 on 2022-05-09 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='категория для темы')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'категория раскрасок',
                'verbose_name_plural': 'категория раскрасок',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='тема раскраски')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='контент для темы')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coloring_pages.category', verbose_name='категория для темы')),
            ],
            options={
                'verbose_name': 'тема для раскрасок',
                'verbose_name_plural': 'тема для раскрасок',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Coloring_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя для раскраски')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото для раскраски')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coloring_pages.tema', verbose_name='тема раскраски')),
            ],
            options={
                'verbose_name': 'картинки для раскрасок',
                'verbose_name_plural': 'картинки для раскрасок',
                'ordering': ['name'],
            },
        ),
    ]
