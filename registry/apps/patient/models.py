from django.contrib.auth.models import User
from django.contrib.gis.db import models


from registry.apps.human_resources.models import Passport, AbstractPerson


class Patient(AbstractPerson):
    passport = models.ForeignKey(
        Passport,
        null=True, blank=True,
        on_delete=models.CASCADE,
        verbose_name='Паспортные данные',
    )

    class Meta:
        db_table = 'patient'


class AdditionalDataPatient(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )
    attribute = models.CharField(
        max_length=50,
        verbose_name='Наименование атрибута',
    )
    value = models.CharField(
        max_length=255,
        verbose_name='Значение атрибута',
    )

    class Meta:
        db_table = 'other_data_patient'
