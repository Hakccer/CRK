# Generated by Django 4.0.4 on 2022-07-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_remove_room_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='messaging',
            name='roo_name',
            field=models.TextField(default='anon'),
        ),
    ]
