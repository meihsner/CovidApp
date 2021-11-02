from django.forms import ModelForm
from .models import Person, City, Laboratory, Hospital


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['name', 'surname', 'gender', 'age', 'address', 'city', 'telephone_number', 'date_of_received_information',
        #           'date_of_positive_result', 'laboratory_performing_tests', 'whereabouts', 'source_of_infection',
        #           'hospitalization', 'hospital', 'supervision', 'quarantine']


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'county', 'province']


class LaboratoryForm(ModelForm):
    class Meta:
        model = Laboratory
        fields = ['name', 'address', 'city']


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'city']
