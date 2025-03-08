from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Ajoute ici les champs personnalisés
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    # Par exemple, un champ pour la date de naissance et un champ pour une photo de profil.
    
    def __str__(self):
        return self.username
