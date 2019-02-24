from django.db import models

from registry.apps.human_resources.models import HealthWorker
from registry.apps.patient.models import Patient


class DoctorSchedule(models.Model):
    health_worker = models.ForeignKey(
        HealthWorker,
        on_delete=models.CASCADE,
        verbose_name='Специалист'
    )
    consult_room = models.PositiveSmallIntegerField(
        verbose_name='Номер кабинета',
    )
    consult_time = models.DateTimeField(
        verbose_name='Время приема',
    )
    patient = models.ForeignKey(
        Patient,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Пациент',
    )

    class Meta:
        db_table = 'doctor_schedule'

