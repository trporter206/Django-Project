# Generated by Django 2.1.7 on 2019-04-10 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barback', '0014_auto_20190409_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='cocktail_image',
            field=models.ImageField(blank=True, null=True, upload_to='cocktail_images/'),
        ),
    ]