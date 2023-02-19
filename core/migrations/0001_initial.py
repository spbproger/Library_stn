# Generated by Django 4.1.6 on 2023-02-18 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/', verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('phone', models.BigIntegerField(verbose_name='Номер телефона')),
                ('status', models.BooleanField(default=True, verbose_name='Активен')),
                ('book_list', models.CharField(max_length=100, verbose_name='Список книг')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('description', models.SlugField(verbose_name='Описание')),
                ('pages', models.PositiveSmallIntegerField(verbose_name='Количество страниц')),
                ('book_num', models.PositiveIntegerField(verbose_name='Количество книг')),
                ('author', models.ManyToManyField(related_name='authors', to='core.author', verbose_name='Авторы')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
