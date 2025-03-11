from django.contrib import admin
from .models import TaskType, Task, Project, ProjectTemplate, TaskTemplate, Tenant

# Register your models here.
admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(ProjectTemplate)
admin.site.register(TaskTemplate)
admin.site.register(Tenant)
