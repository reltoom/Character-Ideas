# Generated by Django 4.2.13 on 2024-05-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0013_alter_character_class_archetype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='class_archetype',
            field=models.CharField(choices=[('Barbarian', 'Barbarian'), ('Bard', 'Bard'), ('Cleric', 'Cleric'), ('Druid', 'Druid'), ('Fighter', 'Fighter'), ('Monk', 'Monk'), ('Paladin', 'Paladin'), ('Ranger', 'Ranger'), ('Rogue', 'Rogue'), ('Sorcerer', 'Sorcerer'), ('Warlock', 'Warlock'), ('Wizard', 'Wizard')], default='Fighter', max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('None', 'None')], default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(choices=[('Dwarf', 'Dwarf'), ('Elf', 'Elf'), ('Half-Elf', 'Half-Elf'), ('Human', 'Human'), ('Halfling', 'Halfling'), ('Gnome', 'Gnome'), ('Half-Orc', 'Half-Orc'), ('Dragonborn', 'Dragonborn'), ('Tiefling', 'Tiefling'), ('Githyanki', 'Githyanki')], default='Human', max_length=50),
        ),
    ]
