# Generated by Django 4.2.13 on 2024-05-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0005_character_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='featured_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='character',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]