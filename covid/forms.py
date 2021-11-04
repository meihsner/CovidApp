from django.forms import ModelForm
from .models import Person, City, Laboratory, Hospital
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class LaboratoryForm(ModelForm):
    class Meta:
        model = Laboratory
        fields = '__all__'


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='username', min_length=5, max_length=32)
    email = forms.EmailField(label='email', required=False)
    first_name = forms.CharField(label='first_name', max_length=32)
    last_name = forms.CharField(label='last_name', max_length=32)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirm password', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class NewUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=32)
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='first_name', max_length=32)
    last_name = forms.CharField(label='last_name', max_length=32)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Użytkownik o tej nazwie już istnieje...")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email już istnieje...")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasła nie pasują do siebie...")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )

        return user

