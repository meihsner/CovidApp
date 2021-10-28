from django.urls import path
from .views import main, add_person, add_laboratory, add_hospital, edit_person, delete_person, add_city


urlpatterns = [
    path('main/', main, name='main'),
    path('add_person/', add_person, name='add_person'),
    path('edit_person/<int:id>/', edit_person, name='edit_person'),
    path('delete_person/<int:id>/', delete_person, name='delete_person'),
    path('add_laboratory/', add_laboratory, name='add_laboratory'),
    path('add_hospital/', add_hospital, name='add_hospital'),
    path('add_city/', add_city, name='add_city')
]