from django.db import models


class CatalogTable(models.Model):
    Name = models.CharField('ФИО / Название предприяти', max_length=255)
    RegDate = models.DateTimeField('Дата записи в справочник')
    Address = models.CharField('Адрес', max_length=255)
    Phone = models.CharField('Телефон', max_length=30)
