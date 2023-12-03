from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse 

# Create your views here.
def home(request):
    return render(request,'website/index.html')

def careers(request):
    return render(request,"website/careers.html")

def tc(request):
    return render(request,"website/tc.html")    

def rc(request):
    return render(request,"website/rc.html")
    
def map(request):
    return render(request,"website/map.html")

def pp(request):
    return render(request,"website/pp.html")    
