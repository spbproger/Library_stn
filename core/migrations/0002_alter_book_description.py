# Generated by Django 4.1.6 on 2023-02-18 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
