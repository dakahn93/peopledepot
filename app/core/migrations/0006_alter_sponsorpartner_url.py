# Generated by Django 4.0.7 on 2022-09-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sponsorpartner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorpartner',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]