from django.shortcuts import render
from .models import Emloyee
# Create your views here.
def Employe(request):
	data = {

	}
	return render(request, 'addemployee.html', data)
