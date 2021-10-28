from django.contrib import admin
from .models import Cities, Laboratories, Hospitals, Persons


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    fields = ['name', 'county', 'province']
    list_filter = ['county', 'province']
    search_fields = ['name']


@admin.register(Laboratories)
class CitiesAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'city']
    list_filter = ['city']
    search_fields = ['name', 'address', 'city']


@admin.register(Hospitals)
class CitiesAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'city']
    list_filter = ['city']
    search_fields = ['name', 'address', 'city']


@admin.register(Persons)
class CitiesAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'gender', 'age', 'city', 'telephone_number', 'date_of_received_information',
              'date_of_positive_result', 'laboratory_performing_tests', 'whereabouts', 'source_of_infection',
              'hospitalization', 'hospital', 'supervision', 'quarantine']
    list_filter = ['gender', 'city', 'laboratory_performing_tests']
    search_fields = ['name', 'surname']
