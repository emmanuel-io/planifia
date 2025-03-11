from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.tenants.models import Tenant

class CustomUser(AbstractUser):
    # Ajoute ici les champs personnalisés
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    # Par exemple, un champ pour la date de naissance et un champ pour une photo de profil.
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE, related_name="users")
    
    def __str__(self):
        return self.username
