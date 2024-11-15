# Generated by Django 5.1.3 on 2024-11-15 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_translations_translation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='translator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.translator', verbose_name='Переводчик'),
        ),
    ]
