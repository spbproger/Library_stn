# Generated by Django 4.1.6 on 2023-03-05 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_author_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='edited',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_num',
            field=models.PositiveIntegerField(verbose_name='Общее количество книг'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='edited',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='core.author', verbose_name='Авторы'),
        ),
    ]
