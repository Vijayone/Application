from django.shortcuts import render

# Create your views here.
def HomeView(request):
	data ={}
	return render(request,'index.html',data)
	
