# Generated by Django 5.2.1 on 2025-05-28 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='availability_from',
            new_name='available_from',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='availability_to',
            new_name='available_to',
        ),
    ]
