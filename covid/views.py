from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Person, City, Hospital, Laboratory
from .forms import PersonForm, CityForm, HospitalForm, LaboratoryForm
from django.contrib.auth.forms import UserCreationForm


@staff_member_required
def user_registration(request):
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('main')
    else:
        new_user = UserCreationForm()
    return render(request, 'registration/register.html', {'form_new_user': new_user})


@login_required
def main(request):
    people = Person.objects.all()
    return render(request, 'main.html', {'people': people})


@login_required
def add_person(request):
    form_person = PersonForm(request.POST or None)
    if form_person.is_valid():
        form_person.save()
        return redirect(main)
    return render(request, 'add_person.html', {'form_person': form_person})


@login_required
def edit_person(request, id):
    person = get_object_or_404(Person, pk=id)
    form_person = PersonForm(request.POST or None, instance=person)
    if form_person.is_valid():
        form_person.save()
        return redirect(main)
    return render(request, 'add_person.html', {'form_person': form_person})


@login_required
def delete_person(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == "POST":
        person.delete()
        return redirect(main)
    return render(request, 'delete_confirm.html', {'person': person})


@login_required
def add_laboratory(request):
    if Laboratory.objects.count() <= 5:
        laboratories = Laboratory.objects.order_by('-id')
    else:
        laboratories = Laboratory.objects.order_by('-id')[0:6]

    form_laboratory = LaboratoryForm(request.POST or None)
    if form_laboratory.is_valid():
        form_laboratory.save()
        return redirect(main)
    return render(request, 'add_laboratory.html', {'form_laboratory': form_laboratory, 'laboratories': laboratories})


@login_required
def add_hospital(request):
    if Hospital.objects.count() <= 5:
        hospitals = Hospital.objects.order_by('-id')
    else:
        hospitals = Hospital.objects.order_by('-id')[0:6]

    form_hospital = HospitalForm(request.POST or None)
    if form_hospital.is_valid():
        form_hospital.save()
        return redirect(main)
    return render(request, 'add_hospital.html', {'form_hospital': form_hospital, 'hospitals': hospitals})


@login_required
def add_city(request):
    if City.objects.count() <= 5:
        cities = City.objects.order_by('-id')
    else:
        cities = City.objects.order_by('-id')[0:6]

    form_city = CityForm(request.POST or None)
    if form_city.is_valid():
        form_city.save()
        return redirect(add_city)
    return render(request, 'add_city.html', {'form_city': form_city, 'cities': cities})
