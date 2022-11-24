from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, wolrd!!!!!")

def listas(request):
    clientes: list[dict] = [
        {"nome": "Eliza", "Carta0": "0000 eeee EEEE 0000"},
        {"nome": "Kaka", "Carta0": "0000 eeee EEEE 0000"},
    ]
    # if id:
    #     return render(request,"lista.html",context={"clientes": clientes})
    


    return render(request,"lista.html",context={"clientes": clientes})