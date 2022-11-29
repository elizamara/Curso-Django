from django.views import View
# from django.views.generic import 
from django.shortcuts import render, get_list_or_404, redirect


from .forms import ClienteForm
from cliente.models import Cliente

# Create your views here.

class Index(View):
    def get(self, request):
        form = ClienteForm()
        clientes =  Cliente.objects.all()
        return render 



def index(request):
    clientes =  Cliente.objects.all() 
    form =  ClienteForm()
    clientes =  Cliente.objects.all()

    if request.method == "POST":
        form= ClienteForm(request, POST)

        if form.is_valid():
            form.save()

        return redirect(to="cliente:index")

    return render(request,"index.html", context={"cliente": clientes })
 


def lista(request):
    return render(request, "lista.html", context={"clientes":clientes, "titulo":"Lista de clientes"})


def detalhe(request, id):
    # cliente = Cliente.objects.get(pk=id)
    cliente = get_list_or_404(Cliente, id=id)
    return render(request, "detalhe.html", context={"cliente": cliente})


def contato(request):
    return render(request, "contatos.html")