from django.urls import path
from . import views


app_name="cliente"


urlpatterns = [
    path("", view=views.Index, name="index"),

    path("lista", views.Listas, name = lista),
    
    path("lista/<int: id>/", views.listas.id)
]

