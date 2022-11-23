from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, wolrd!!!!!")

def listas(request):
    return render(request,"lista.html",context={})