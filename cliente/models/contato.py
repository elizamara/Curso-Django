from django.db import models
from .cliente import Cliente


TIPO= [
    ("C", "Comercial"), ("P", "Pessoal")
]

class Contato(models.Model):
    tipo = models.CharField(max_length=1, blank=False, choices=TIPO)
    telefone = models.CharField(max_length=9 , blank=False)
    dd = models.CharField(max_length=3, blank=True, null=True)
    email= models.EmailField(max_length=180)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo

    
    class Meta:
        ordering= ["cliente"]