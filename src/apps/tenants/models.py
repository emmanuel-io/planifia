from django.db import models
from ...core.models import BaseModel

class Tenant(BaseModel):
    """Représente un espace isolé de données pour un client SaaS"""
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"
        db_table = "tenant"
