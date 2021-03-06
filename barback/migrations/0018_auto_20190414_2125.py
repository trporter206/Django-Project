# Generated by Django 2.1.7 on 2019-04-15 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barback', '0017_auto_20190414_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
