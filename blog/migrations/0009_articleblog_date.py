# Generated by Django 2.2.2 on 2019-06-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190616_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleblog',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
