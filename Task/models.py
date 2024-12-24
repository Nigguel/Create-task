"""     Modelos     """

from django.db import models


# Create your models here.
class Tasks(models.Model):
    """
    Modelo para definir la estructura de las tareas
    """

    task_name = models.CharField(max_length=255)
    task_description = models.CharField(max_length=1000, blank=True)
    task_date = models.DateTimeField(auto_now_add=True)
    task_check = models.BooleanField(default=False)

    def __str__(self):
        return str(self.task_name)
