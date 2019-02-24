from datetime import date, datetime

from django.contrib.gis.geos import Point

from registry.apps.ambulance.models import AmbulanceRequest, AmbulanceCrew
from registry.apps.human_resources.models import Passport, QualificMedic, QualificSupportStuff, HealthWorker, \
    SupportStuff
from registry.apps.material_resurces.models import Automobile
from registry.apps.patient.models import Patient, AdditionalDataPatient


def build_automobile():
    Automobile.objects.bulk_create([
        Automobile(
            mark='ГАЗЕЛЬ',
            model='3110',
            reg_number='т234нв151',
            geo_position=Point([39.700093, 47.230454])
        ),
        Automobile(
            mark='Mercedes',
            model='V2',
            reg_number='в204кт141',
            geo_position=Point([39.800093, 47.230454])
        ),
    ])


def build_passport():
    Passport.objects.bulk_create([
        Passport(
            name='Иван',
            surname='Иванов',
            patronymic='Иванович',
            serial='61 10',
            number='232324',
            date_issue=date.fromisoformat('2018-01-01'),
            issued_by='Отделом УФМС',
            registration='Ростов, Садовая 35, кв 43',
        ),
        Passport(
            name='Петр',
            surname='Петров',
            patronymic='Петрович',
            serial='61 10',
            number='256324',
            date_issue=date.fromisoformat('2012-05-14'),
            issued_by='Отделом УФМС',
            registration='Ростов, Капустина 33, кв 2',
        ),
        Passport(
            name='Максим',
            surname='Максимов',
            patronymic='Максимович',
            serial='61 10',
            number='256333',
            date_issue=date.fromisoformat('2012-03-14'),
            issued_by='Отделом УФМС',
            registration='Ростов, Красноармейская 23, кв 11',
        ),
        Passport(
            name='Анна',
            surname='Ижевская',
            patronymic='Денисовна',
            serial='61 10',
            number='2563683',
            date_issue=date.fromisoformat('2012-04-14'),
            issued_by='Отделом УФМС',
            registration='Ростов, Чернышевский 18, кв 2',
        ),
        Passport(
            name='Кристина',
            surname='Петренко',
            patronymic='Олеговна',
            serial='61 10',
            number='463683',
            date_issue=date.fromisoformat('2012-01-14'),
            issued_by='Отделом УФМС',
            registration='Ростов, Чернышевский 18, кв 2',
        ),
        Passport(
            name='Алиса',
            surname='Ивлеева',
            patronymic='Кирилловна',
            serial='61 10',
            number='453283',
            date_issue=date.fromisoformat('2011-03-12'),
            issued_by='Отделом УФМС',
            registration='Ростов, Павлова 123, кв 4',
        ),
        Passport(
            name='Федор',
            surname='Тимофеев',
            patronymic='Алексеевич',
            serial='61 10',
            number='1233438',
            date_issue=date.fromisoformat('2011-03-12'),
            issued_by='Отделом УФМС',
            registration='Ростов, Павлова 123, кв 4',
        ),
    ])


def build_QualificMedic():
    QualificMedic.objects.bulk_create([
        QualificMedic(label='Терапевт'),
        QualificMedic(label='Медсестра'),
        QualificMedic(label='Хирург'),
        QualificMedic(label='Дантист'),
    ])


def build_QualificSupportStuff():
    QualificSupportStuff.objects.bulk_create([
        QualificSupportStuff(label='Водитель'),
        QualificSupportStuff(label='Охранник'),
    ])


def build_HealthWorker():
    HealthWorker.objects.bulk_create([
        HealthWorker(passport=Passport.objects.get(name='Алиса', number='453283'),
                     qualification=QualificMedic.objects.get(label='Медсестра')),
        HealthWorker(passport=Passport.objects.get(name='Кристина', number='463683'),
                     qualification=QualificMedic.objects.get(label='Медсестра')),
        HealthWorker(passport=Passport.objects.get(name='Анна', number='2563683'),
                     qualification=QualificMedic.objects.get(label='Терапевт')),
        HealthWorker(passport=Passport.objects.get(name='Максим', number='256333'),
                     qualification=QualificMedic.objects.get(label='Хирург')),
    ])


def build_SupportStuff():
    SupportStuff.objects.bulk_create([
        SupportStuff(passport=Passport.objects.get(name='Петр', number='256324'),
                     qualification=QualificSupportStuff.objects.get(label='Водитель')),
        SupportStuff(passport=Passport.objects.get(name='Иван', number='232324'),
                     qualification=QualificSupportStuff.objects.get(label='Водитель'))
    ])


def build_AmbulanceCrew():
    a1 = AmbulanceCrew.objects.create(automobile=Automobile.objects.get(reg_number='т234нв151'),
                                      driver=SupportStuff.objects.get(passport__number='256324'))
    a2 = AmbulanceCrew.objects.create(automobile=Automobile.objects.get(reg_number='т234нв151'),
                                      driver=SupportStuff.objects.get(passport__number='256324'))

    a1.group_crew.add(
        HealthWorker.objects.get(passport__name='Алиса', passport__number='453283'),
        HealthWorker.objects.get(passport__name='Анна', passport__number='2563683'),
    )

    a2.group_crew.add(
        HealthWorker.objects.get(passport__name='Максим', passport__number='256333'),
        HealthWorker.objects.get(passport__name='Алиса', passport__number='453283'),
    )

    return [a1, a2]


def build_Patient():
    p1 = Patient(passport=Passport.objects.get(name='Федор', number='1233438'))
    p2 = Patient()
    p3 = Patient()
    Patient.objects.bulk_create([p1, p2, p3])

    AdditionalDataPatient.objects.bulk_create([
        AdditionalDataPatient(patient=p1),
    ])
    AdditionalDataPatient.objects.bulk_create([
        AdditionalDataPatient(patient=p2, attribute='Татуировка на шее', value='Дракон'),
        AdditionalDataPatient(patient=p2, attribute='Куртка', value='Черная'),
        AdditionalDataPatient(patient=p2, attribute='Штаны', value='Спортивные'),
        AdditionalDataPatient(patient=p2, attribute='Волосы', value='Светлые'),
    ])
    AdditionalDataPatient.objects.bulk_create([
        AdditionalDataPatient(patient=p3, attribute='Татуировка на лбу', value='666'),
        AdditionalDataPatient(patient=p3, attribute='Кофта', value='Красная'),
        AdditionalDataPatient(patient=p3, attribute='Штаны', value='Джинсовые'),
        AdditionalDataPatient(patient=p3, attribute='Волосы', value='Тёмные'),
        AdditionalDataPatient(patient=p3, attribute='Очки', value='Тёмные'),
    ])

    return [p1, p2, p3]


def build_AmbulanceRequest(patients, crews):
    # patients = Patient.objects.all()
    # crews = AmbulanceCrew.objects.all()
    a1 = AmbulanceRequest.objects.create(patient=patients[0],
                                         symptoms='Тошнота, боль в животе',
                                         geo_from=Point([39.710093, 47.220454]),
                                         geo_to=Point([39.770093, 47.140454]),
                                         )
    a1.crew.add(crews[0])
    a2 = AmbulanceRequest.objects.create(patient=patients[1],
                                         symptoms='Инсульт',
                                         geo_from=Point([39.760093, 47.260454]),
                                         geo_to=Point([39.420093, 47.130454]),
                                         )
    a2.crew.add(crews[0])
    a3 = AmbulanceRequest.objects.create(patient=patients[2],
                                         symptoms='Температура 39',
                                         geo_from=Point([39.735093, 47.220454]),
                                         geo_to=Point([39.550093, 47.230454]),
                                         )
    a3.crew.add(crews[1])


# from registry.data.init_data import start_building as i; i()
def start_building():
    build_automobile()
    build_passport()
    build_QualificMedic()
    build_QualificSupportStuff()
    build_HealthWorker()
    build_SupportStuff()

    crews = build_AmbulanceCrew()
    patients = build_Patient()
    build_AmbulanceRequest(patients, crews)
