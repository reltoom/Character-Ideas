# Generated by Django 4.2.13 on 2024-05-22 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0007_rename_image_character_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='featured_image',
            new_name='character_picture',
        ),
    ]
