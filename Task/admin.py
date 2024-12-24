"""     Admin     """

from django.contrib import admin
from .models import Tasks


class TaskAdmin(admin.ModelAdmin):
    """
    Personalizando el modelo de Task
    """

    list_display = ["task_name", "task_description", "task_date"]


# Register your models here.
admin.site.register(Tasks, TaskAdmin)
