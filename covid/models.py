from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):
    PROVINCE = {
        (1, 'Dolnośląskie'),
        (2, 'Kujawsko-pomorskie'),
        (3, 'Lubelskie'),
        (4, 'Lubuskie'),
        (5, 'Łódzkie'),
        (6, 'Małopolskie'),
        (7, 'Mazowieckie'),
        (8, 'Opolskie'),
        (9, 'Podkarpackie'),
        (10, 'Podlaskie'),
        (11, 'Pomorskie'),
        (12, 'Śląskie'),
        (13, 'Świętokrzyskie'),
        (14, 'Warmińsko-mazurskie'),
        (15, 'Wielkopolskie'),
        (16, 'Zachodniopomorskie'),
    }

    name = models.CharField(max_length=32)
    county = models.CharField(max_length=32)
    province = models.PositiveSmallIntegerField(choices=PROVINCE, default=1)

    def __str__(self):
        return self.name_province()

    def name_province(self):
        return "{}".format(self.name)


class Laboratory(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='LaboratoryCity')

    def __str__(self):
        return self.name_city()

    def name_city(self):
        return "{} ({})".format(self.name, self.city)


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='HospitalCity')

    def __str__(self):
        return self.name_city()

    def name_city(self):
        return "{} ({})".format(self.name, self.city)


class Person(models.Model):
    GENDER = {
        (1, 'Mężczyzna'),
        (2, 'Kobieta'),
        (3, 'inna')
    }
    BINARY = {
        (0, 'Nie'),
        (1, 'Tak')
    }

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=60)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='city')
    telephone_number = PhoneNumberField()

    date_of_received_information = models.DateField(null=True, blank=True)
    date_of_positive_result = models.DateField(null=True, blank=True)
    laboratory_performing_tests = models.ForeignKey(Laboratory, on_delete=models.PROTECT, related_name='laboratory')
    whereabouts = models.ForeignKey(City, on_delete=models.PROTECT, related_name='whereabouts')
    source_of_infection = models.TextField(null=True, blank=True)

    hospitalization = models.PositiveSmallIntegerField(choices=BINARY, default=0)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, related_name='hospital', null=True, blank=True)
    supervision = models.PositiveSmallIntegerField(choices=BINARY, default=0)
    quarantine = models.PositiveSmallIntegerField(choices=BINARY, default=0)

    who_added = models.CharField(max_length=32, default="None")

    def __str__(self):
        return self.name_surname_age()

    def name_surname_age(self):
        return "{} {} ({})".format(self.name, self.surname, self.age)
