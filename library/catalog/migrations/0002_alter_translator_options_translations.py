# Generated by Django 5.1.2 on 2024-10-22 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='translator',
            options={'verbose_name': 'переводчик', 'verbose_name_plural': 'Переводчики'},
        ),
        migrations.CreateModel(
            name='Translations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('translator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.translator')),
            ],
        ),
    ]