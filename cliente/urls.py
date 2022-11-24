from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    # path("lista/<int:id>/", views.listas)
    path("lista", views.listas)
]

