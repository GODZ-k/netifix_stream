# Generated by Django 4.2.4 on 2023-11-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0008_hot_thrills_clip_poster_alter_hot_thrills_clip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hot_thrills',
            name='clip',
            field=models.FileField(blank=True, help_text='If not clip url (Optional)', null=True, upload_to='movie_media'),
        ),
    ]
