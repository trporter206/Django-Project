# Generated by Django 2.1.7 on 2019-04-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barback', '0021_auto_20190422_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='public',
            field=models.BooleanField(null=True),
        ),
    ]
