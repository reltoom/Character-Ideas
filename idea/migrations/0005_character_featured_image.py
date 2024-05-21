# Generated by Django 4.2.13 on 2024-05-21 06:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0004_alter_character_options_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
