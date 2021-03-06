# Generated by Django 2.2.2 on 2019-06-15 15:47

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=blog.models.image_folder)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('description_short', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('author', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
