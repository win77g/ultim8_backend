# Generated by Django 2.2.2 on 2019-06-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Сервис', 'verbose_name_plural': 'Сервисы'},
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
