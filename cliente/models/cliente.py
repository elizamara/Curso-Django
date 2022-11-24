from django.db import models

# Create your models here.
class cliente(models.Model):

    tipo_pessoa= [
        ("F", "Fisica"), ("J", "Juridica")
    ]

    nome = models.CharField(max_length=100, null= False)
    cpf_cnpj = models.CharField(max_length=14, null= False)
    tipo = models.CharField(max_length= 1, choices= tipo_pessoa)
    dt_criacao = models.DateTimeField(verbose_name="Data de criação", auto_now_add= True)
    dt_alteracao= models.DateTimeField(verbose_name="Data de alteração", auto_now= True)


    def __str__(self):
        return self.nome