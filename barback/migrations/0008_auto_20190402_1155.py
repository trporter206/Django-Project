# Generated by Django 2.2 on 2019-04-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barback', '0007_auto_20190402_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='cocktail_image',
            field=models.ImageField(blank=True, null=True, upload_to='cocktail_images/'),
        ),
    ]
