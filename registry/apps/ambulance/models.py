from django.contrib.gis.db import models

from registry.apps.human_resources.models import SupportStuff, HealthWorker
from registry.apps.material_resurces.models import Automobile
from registry.apps.patient.models import Patient


class AmbulanceCrew(models.Model):
    driver = models.ForeignKey(
        SupportStuff,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Водитель'
    )
    group_crew = models.ManyToManyField(
        HealthWorker,
        db_column='group_crew',
        verbose_name='Группа мед. персонала'
    )
    automobile = models.ForeignKey(
        Automobile,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Автомобиль'
    )

    class Meta:
        db_table = 'ambulance_crew'


class AmbulanceRequest(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='Пациент',
    )
    symptoms = models.CharField(
        max_length=255,
        verbose_name='Симптомы больного'
    )
    crew = models.ManyToManyField(
        AmbulanceCrew
    )
    geo_from = models.PointField(
        verbose_name='Геопозиция машины',
        null=True, blank=True,
    )
    geo_to = models.PointField(
        verbose_name='Геопозиция пациента',
    )
    date_call = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время вызова',
    ),
    date_arrive = models.DateTimeField(
        null=True, blank=True,
        verbose_name='Время прибытия',
    )

    class Meta:
        db_table = 'request_ambulance'
