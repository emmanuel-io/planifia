from enum import Enum
from django.contrib.auth import get_user_model
from django.db import models
from core.models import BaseTenantModel

User = get_user_model()

class Project(BaseTenantModel):
    """Project optionally based on a template with automatically generated tasks."""
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    manager = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    template = models.ForeignKey("ProjectTemplate", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project"

class ProjectTemplate(BaseTenantModel):
    """Project template."""
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Template Project: {self.name}"

    class Meta:
        db_table = "template_project"
