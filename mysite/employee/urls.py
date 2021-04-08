from django.urls import path

from . import views
urlpatterns = [

path('addemployee/', views.Employe, name='employee')
]

