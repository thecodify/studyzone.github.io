# Generated by Django 5.0.7 on 2024-07-27 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_places'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
    ]
