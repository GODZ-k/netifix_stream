# Generated by Django 4.2.4 on 2023-11-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0010_remove_hot_thrills_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='poster3',
        ),
    ]