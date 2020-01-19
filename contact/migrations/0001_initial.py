# Generated by Django 2.2.2 on 2019-07-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('control', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
