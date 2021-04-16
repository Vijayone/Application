from django.urls import path

from . import views
urlpatterns = [

path('employeeinfo/',views.Employe, name='employeeinfo'), # view the employee page information
path('addemployee/', views.EmployeAdd, name='employee'),# Addform of employee
path('addemp/',views.EmployeAdd, name= 'addemployee'), # operations of Adding
]

