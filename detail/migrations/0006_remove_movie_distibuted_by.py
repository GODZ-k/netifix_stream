# Generated by Django 4.2.4 on 2023-11-18 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0005_tags_movie_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='distibuted_by',
        ),
    ]
