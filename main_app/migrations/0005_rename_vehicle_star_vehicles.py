# Generated by Django 4.0.1 on 2022-01-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_combat_style_vehicle_remove_star_combat_style_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='star',
            old_name='vehicle',
            new_name='vehicles',
        ),
    ]