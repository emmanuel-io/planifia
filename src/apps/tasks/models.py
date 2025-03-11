from enum import Enum
from django.contrib.auth import get_user_model
from django.db import models
from ....core.models import BaseTenantModel

User = get_user_model()

class TaskStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class TaskType(BaseTenantModel):
    """Reusable task type."""
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "task_type"

class TaskTemplate(BaseTenantModel):
    """Tâches par défaut associées à un modèle de projet."""
    template = models.ForeignKey("ProjectTemplate", on_delete=models.CASCADE, related_name="tasks")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)

    def __str__(self):
        return f"Template model: {self.template.name} -> Type: {self.task_type.name}"

    class Meta:
        db_table = "template_task"

class Task(BaseTenantModel):
    """Task associated to a project."""
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="tasks")
    task_type = models.ForeignKey(TaskType, null=True, on_delete=models.CASCADE)  # Utilisation des types de tâches
    name = models.CharField(max_length=64)
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, )
    actual_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    status = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in TaskStatus],
        default=TaskStatus.PENDING.value
    )

    def __str__(self):
        return f"{self.name} - {self.project.name}"

    class Meta:
        db_table = "task"


