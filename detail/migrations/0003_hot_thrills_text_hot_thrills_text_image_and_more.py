# Generated by Django 4.2.4 on 2023-11-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0002_alter_hot_thrills_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='hot_thrills',
            name='text',
            field=models.CharField(blank=True, help_text='If not text_image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hot_thrills',
            name='text_image',
            field=models.URLField(blank=True, help_text='Image should be .png', null=True),
        ),
        migrations.AddField(
            model_name='hot_thrills',
            name='text_upload_image',
            field=models.ImageField(blank=True, help_text='If not have text_image url', null=True, upload_to='movie_media'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_match',
            field=models.CharField(help_text='Ex: 67 ,Enter only number', max_length=100),
        ),
    ]
