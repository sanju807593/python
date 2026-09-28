from django.urls import path
from .views import add_student


urlpatterns = [
    path('', add_student, name='home'),
    path('add_student/', add_student, name='add_student')
]