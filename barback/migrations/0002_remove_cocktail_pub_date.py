# Generated by Django 2.1.7 on 2019-03-22 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='pub_date',
        ),
    ]
