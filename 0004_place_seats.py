# Generated by Django 5.0.7 on 2024-07-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_place_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='seats',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
