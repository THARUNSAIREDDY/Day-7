from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h2 style='color:blue;background-color:green'> welcome to you.</h2>")



def chk(request):
	return HttpResponse("<script>alert('hi good afternoon')</scipt><h2> hello.</h2>")


def homepage(request):
	return render(request,'ht/homepage.html')


def logp(re):
	return render(re,'ht/login.html')


def reg(re):
	return render(re,'ht/register.html')