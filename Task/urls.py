"""     Task urls     """

from django.urls import path
from . import views

app_name = "tasks"  # pylint: disable=C0103

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>", views.detalle, name="detalle"),
    path("formulario", views.formulario, name="formulario"),
    path("<int:task_id>/actualizar", views.actualizar, name="actualizar"),
    path("<int:task_id>/eliminar", views.eliminar, name="eliminar"),
]
