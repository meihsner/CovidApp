from django.contrib import admin
from .models import City, Laboratory, Hospital, Person


@admin.register(City)
class CitiesAdmin(admin.ModelAdmin):
    fields = ['name', 'county', 'province']
    list_filter = ['county', 'province']
    search_fields = ['name']


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'city']
    list_filter = ['city']
    search_fields = ['name', 'address', 'city']


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'city']
    list_filter = ['city']
    search_fields = ['name', 'address', 'city']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'gender', 'age', 'address', 'city', 'telephone_number', 'date_of_received_information',
              'date_of_positive_result', 'laboratory_performing_tests', 'whereabouts', 'source_of_infection',
              'hospitalization', 'hospital', 'supervision', 'quarantine', 'who_added']
    list_filter = ['gender', 'city', 'laboratory_performing_tests']
    search_fields = ['name', 'surname']
