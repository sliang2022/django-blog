# Generated by Django 3.1.5 on 2023-11-22 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Poll',
        ),
    ]