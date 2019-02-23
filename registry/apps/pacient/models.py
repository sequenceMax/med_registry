from django.contrib.gis.db import models


class Pacient(models.Model):
    name = models.CharField()
    surname = models.CharField()
    patronymic = models.CharField()

    other_data = models.ForeignKey()

    passport = models.ForeignKey()

    is_alive = models.BooleanField()


class AdditionalDataPacient(models.Model):
    attribute = models.CharField()
    value = models.CharField()
    date_create = models.DateField()


class Passport(models.Model):
    serial = models.IntegerField()
    number = models.IntegerField()
    date_issue = models.DateField()

    issued_by = models.CharField()

    registration = models.CharField()


class AmbulancePacient(Pacient):
    geo = models.PointField()


