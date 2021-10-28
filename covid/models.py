from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cities(models.Model):
    name = models.CharField(max_length=32)
    county = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

    def __str__(self):
        return self.name_province()

    def name_province(self):
        return "{} ({})".format(self.name, self.province)


class Laboratories(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    city = models.ForeignKey(Cities, on_delete=models.PROTECT, related_name='LaboratoryCity')

    def __str__(self):
        return self.name_city()

    def name_city(self):
        return "{} ({})".format(self.name, self.city)


class Hospitals(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    city = models.ForeignKey(Cities, on_delete=models.PROTECT, related_name='HospitalCity')

    def __str__(self):
        return self.name_city()

    def name_city(self):
        return "{} ({})".format(self.name, self.city)


class Persons(models.Model):
    GENDER = {
        (1, 'M'),
        (2, 'K'),
        (3, 'other')
    }
    BINARY = {
        (0, 'Nie'),
        (1, 'Tak')
    }

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    age = models.PositiveSmallIntegerField()
    city = models.ForeignKey(Cities, on_delete=models.PROTECT, related_name='city')
    telephone_number = PhoneNumberField()

    date_of_received_information = models.DateField(null=True, blank=True)
    date_of_positive_result = models.DateField(null=True, blank=True)
    laboratory_performing_tests = models.ForeignKey(Laboratories, on_delete=models.PROTECT, related_name='laboratory')
    whereabouts = models.ForeignKey(Cities, on_delete=models.PROTECT, related_name='whereabouts')
    source_of_infection = models.TextField(null=True, blank=True)

    hospitalization = models.PositiveSmallIntegerField(choices=BINARY, default=0)
    hospital = models.ForeignKey(Hospitals, on_delete=models.PROTECT, related_name='hospital', null=True, blank=True)
    supervision = models.PositiveSmallIntegerField(choices=BINARY, default=0)
    quarantine = models.PositiveSmallIntegerField(choices=BINARY, default=0)

    def __str__(self):
        return self.name_surname_age()

    def name_surname_age(self):
        return "{} {} ({})".format(self.name, self.surname, self.age)
