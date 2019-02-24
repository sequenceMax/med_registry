from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Passport(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Имя',
    )
    surname = models.CharField(
        max_length=20,
        verbose_name='Фамилия',
    )
    patronymic = models.CharField(
        max_length=20,
        verbose_name='Отчество',
    )
    serial = models.CharField(
        max_length=10,
        verbose_name='Серия',
    )
    number = models.CharField(
        max_length=10,
        verbose_name='Номер',
    )
    date_issue = models.DateField(
        verbose_name='Дата выдачи',
    )
    issued_by = models.CharField(
        max_length=255,
        verbose_name='Выдан',
    )
    registration = models.CharField(
        max_length=255,
        verbose_name='Регистрация',
    )

    class Meta:
        db_table = 'passport'


class AbstractPerson(models.Model):
    passport = models.ForeignKey(
        Passport,
        on_delete=models.CASCADE,
        verbose_name='Паспортные данные',
    )
    user_create = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Кем создан',
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    user_update = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Кем обновлен',
    )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата редактирования',
    )
    date_archive = models.DateTimeField(
        null=True,
        verbose_name='Дата удаления',
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.date_archive = datetime.now()
        self.save()


class AbstractQualification(models.Model):
    label = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Квалификация'
    )

    class Meta:
        abstract = True


class QualificMedic(AbstractQualification):
    class Meta:
        db_table = 'qualific_medic'


class QualificSupportStuff(AbstractQualification):
    class Meta:
        db_table = 'qualific_stuff'


class HealthWorker(AbstractPerson):
    qualification = models.ForeignKey(
        QualificMedic,
        on_delete=models.CASCADE,
        verbose_name='Квалификация'
    )
    prev_id = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.CASCADE,
        db_column='prev_id',
        verbose_name='Предыдущая запись',
    )

    class Meta:
        db_table = 'health_worker'


class SupportStuff(AbstractPerson):
    qualification = models.ForeignKey(
        QualificSupportStuff,
        on_delete=models.CASCADE,
        verbose_name='Квалификация'
    )
    prev_id = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Предыдущая запись',
    )

    class Meta:
        db_table = 'support_stuff'
