from django.shortcuts import render
from django.http import HttpResponse


def index4(request):
    return render(request,'index4.html')



def index5(request):
    return render(request,'index5.html')


def index6(request):
    return HttpResponse('IF YOU JUDGE PEPOLE, YOU HAVE NO TIME TO LOVE THEM')





