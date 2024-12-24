"""     Task Views"""

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Tasks


# Create your views here.
def index(request):
    """
    Index
    """
    tasks = Tasks.objects.all()  # pylint: disable=E1101

    return render(request, "index.html", context={"tasks": tasks})


def detalle(request, task_id):
    """
    detalle
    """
    task = get_object_or_404(Tasks, id=task_id)

    return render(request, "detalle.html", context={"task": task})


def actualizar(request, task_id):
    """
    Actualizar
    """
    task = get_object_or_404(
        Tasks, id=task_id
    )  # Obtiene la instancia de la tarea correspondiente al task_id, o devuelve un error 404
    # si no se encuentra.
    if (
        request.method == "POST"
    ):  # Verifica si el método de la solicitud es POST, lo que indica que el formulario ha
        # sido enviado.
        task.task_name = request.POST[
            "task_name"
        ]  # Actualiza el nombre de la tarea con el valor recibido del formulario.
        task.task_description = request.POST[
            "task_description"
        ]  # Actualiza la descripción de la tarea con el valor recibido del formulario.
        task.task_check = (
            request.POST.get("task_check", False) == "on"
        )  # Actualiza el estado de la tarea (completada o no) basado en si el checkbox fue
        # marcado en el formulario.
        task.save()  # Guarda los cambios en la base de datos.
        return redirect(
            "tasks:detalle", task_id=task_id
        )  # Redirige a la vista de detalle de la tarea una vez que se hayan guardado los cambios.
    return render(
        request, "actualizar.html", context={"task": task}
    )  # Si el método de la solicitud no es POST, renderiza la plantilla 'actualizar.html' pasando
    # la instancia de la tarea.


def formulario(request):
    """
    Formulario
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks")
    else:
        form = TaskForm()

    return render(request, "task_form.html", context={"form": form})


def eliminar(request, task_id):
    """
    eliminar tarea
    """
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:index")
    return render(request, "eliminar.html", context={"task": task})
