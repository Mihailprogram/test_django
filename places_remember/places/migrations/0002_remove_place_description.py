# Generated by Django 4.2 on 2023-04-26 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='description',
        ),
    ]