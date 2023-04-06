from django.contrib import admin
from task_manager.models import TaskModel

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','priority', 'deadline')


admin.site.register(TaskModel, TaskAdmin)