# Generated by Django 3.0.3 on 2020-02-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, verbose_name='ФИО / Название предприяти')),
                ('RegDate', models.DateTimeField(verbose_name='Дата записи в справочник')),
                ('Address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('Phone', models.CharField(max_length=30, verbose_name='Телефон')),
            ],
        ),
    ]
