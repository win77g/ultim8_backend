# Generated by Django 2.2.2 on 2019-06-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20190614_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='description_short',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
