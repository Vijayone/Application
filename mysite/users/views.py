from django.shortcuts import render,redirect
from . models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def Register(request):
	data ={}
	try:
		if request.method == 'POST':
			user_data = User.objects.filter(username=request.POST['username'])
			if user_data:
				raise NameError('oop!,this username is already user!!')
				return redirect('/register')
			else:
				user_data = User(
	              username=request.POST['username'],
	              phone=request.POST['phone'],
	              )
				user_data.set_password(request.POST['password'])
				user_data.save()
				messages.info(request,'Register Successfully')
				return redirect('/login')
	except Exception as e:
		messages.error(request,e)


	return render(request,'register.html',data)


def Login(request):
	data={}
	try:
		if request.method == 'POST':

			login_user = authenticate(username=request.POST['username'], password =request.POST['password'])
			if login_user is not None:
				login(request, login_user)
				messages.success(request,'login successfully')
				return redirect('/')
			else:
				messages.error(request,'login failed')
				return redirect('/login')

	except Exception as e:
		messages.error(request,"oop!, current user is logged successfully")
		return redirect('/login')

	return render(request,'login.html',data)

def Logout(request):
	logout(request)
	return redirect('/')