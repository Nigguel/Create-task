"""     Formularios     """

from django.forms import ModelForm

from . import models


class TaskForm(ModelForm):
    """modelo del Formulario"""

    class Meta:
        """Clase meta"""

        model = models.Tasks
        fields = ["task_name", "task_description"]
