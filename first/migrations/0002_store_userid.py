# Generated by Django 4.0.4 on 2022-07-16 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='userid',
            field=models.TextField(default=''),
        ),
    ]