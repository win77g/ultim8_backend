# Generated by Django 2.2.2 on 2019-06-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190616_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleblog',
            name='sidebar',
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
    ]
