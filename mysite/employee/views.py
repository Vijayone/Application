from django.shortcuts import render,redirect
from .models import Emloyee
from django.contrib import messages
from users.models import User
# Create your views here.
def Employe(request):
	employee_data = Emloyee.objects.all()
	data = {
	'employee_data':employee_data

	}
	return render(request, 'employeeinfo.html', data)

def EmployeAdd(request):
	user = request.user.id
	user_detail = User.objects.all()
	data ={
	 'user' : user,
	 'user_detail': user_detail
	}
	try:
		if request.method == 'POST':

			employee_user = Emloyee(
				user_id  = request.user.id,
				full_name = request.POST['full_name'],
				department = request.POST['department'],
				salary =  request.POST['salary'],
				is_employee = True
				)
			employee_user.save()
			messages.success(request," successfully as employee added")
			return redirect('/employeeinfo')
	except Exception as e:
		messages.error(request, e)
		return redirect('/addemployee')

	return render(request,'addemployee.html',data)