from django.contrib.gis.db import models


class Automobile(models.Model):
    mark = models.CharField(
        max_length=20,
        verbose_name='Марка'
    )
    model = models.CharField(
        max_length=20,
        verbose_name='Модель'
    )
    reg_number = models.CharField(
        max_length=15,
        verbose_name='Регистрационный номер'
    )
    geo_position = models.PointField(
        verbose_name='Текущее местонахождение'
    )

    class Meta:
        db_table = 'automobile'
