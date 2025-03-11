from uuid import uuid4
from django.db import models
from django.utils.timezone import now

class BaseModel(models.Model):
    """Modèle abstrait avec `created_at` et `updated_at`."""
    uuid = models.UUIDField(default=uuid4, unique=True, null= True, editable=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseTenantModel(BaseModel):
    """Modèle abstrait pour inclure Tenant sans répéter le code."""
    tenant = models.ForeignKey("Tenant", null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
