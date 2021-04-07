from django.urls import path
from . import views
urlpatterns =[

path('register/',views.Register,name='Register'),# view only register page
path('login/',views.Login,name='Login'),# view only login page
path('registeruser/',views.Register,name='RegisterUser'),# perform create user url
path('loginuser/',views.Login,name='Loginuser'), # perform login operations
path('logout/',views.Logout,name='Logout') ,#,#  logout operation  page

]

