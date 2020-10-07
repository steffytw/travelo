from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def home(request):
	return HttpResponse('HELLO WORLD')


def index(request):
    return render(request,'traveloApp/index.html')