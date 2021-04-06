from django.shortcuts import render

# Create your views here.
def Register(request):
	data ={}
	return render(request,'register.html',data)