# Generated by Django 4.2.4 on 2023-11-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0007_hot_thrills_clip_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='hot_thrills',
            name='clip_poster',
            field=models.URLField(blank=True, help_text='Poster url (Optional)', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hot_thrills',
            name='clip',
            field=models.FileField(help_text='If not clip url (Optional)', upload_to='movie_media'),
        ),
        migrations.AlterField(
            model_name='hot_thrills',
            name='clip_url',
            field=models.URLField(blank=True, help_text='If not clip', max_length=500, null=True),
        ),
    ]
