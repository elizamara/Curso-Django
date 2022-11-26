from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

from cliente.models import Cliente

# Create your views here.
def Index(request):
    tf request.method == "POST":
    nome = request.POST["nome"]
    return render(request, "index.html")


def Lista(request):
    clientes =  Cliente.objects.all()

def Listas(request):
    clientes: list[dict] = [
        {"nome": "Eliza", "Carta0": "0000 eeee EEEE 0000"},
        {"nome": "Kaka", "Carta0": "0000 eeee EEEE 0000"},
    ]
    # if id:
    #     return render(request,"lista.html",context={"clientes": clientes})
    return render(request,"lista.html",context={"clientes": clientes})


def Detalhe(request, id):
    cliente = Cliente.objects.get(pk=id)
    # cliente = get_list_or_404(Cliente, id=id)
    return render(request, "detalhe.html", context={"cliente": cliente})
