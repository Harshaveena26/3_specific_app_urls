from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')

def index3(request):
    return HttpResponse('love your slef')


