# Generated by Django 4.1.6 on 2023-03-13 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_reader_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='status',
        ),
    ]