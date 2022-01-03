from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    try:
        x=int(request.GET["t1"])
        y = int(request.GET["t2"])
        z=x+y
        res=HttpResponse("sum is :"+str(z))
        return res
    except(ValueError):
        return render(request, 'input.html')