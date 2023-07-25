from django.shortcuts import render
from django.http import HttpResponse

def index7(request):
    return render(request,'index7.html')

def index8(request):
    return render(request,'index8.html')


def index9(requext):
    return HttpResponse('<h1> Music is the best solution to any problem </h1>')





