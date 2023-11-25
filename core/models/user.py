"""
Database models.
"""
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from uploader.models import Image


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""
    CAMPI_CHOICES = [
        ('AL', 'Abelardo Luz '),
        ('AR', 'Araquari'),
        ('BL', 'Blumenau'),
        ('BR', 'Brusque'),
        ('CA', 'Camboriú'),
        ('CO', 'Concórdia'),
        ('FR', 'Fraiburgo '),
        ('IB', 'Ibirama'),
        ('LU', 'Luzerna'),
        ('RS', 'Rio do Sul '),
        ('CA', 'Camboriú'),
        ('SR', 'Santa Rosa do Sul'),
        ('SB', 'São Bento do Sul'),
        ('SF', 'São Francisco do Sul'),
        ('SO', 'Sombrio '),
        ('VI', 'Videira'),
    ]
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    telefone = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    telefone = models.CharField(max_length=20, blank=True)
    curriculo_lattes = models.CharField(max_length=255, blank=True)
    formacao = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    campus = models.CharField(max_length=2, choices=CAMPI_CHOICES, default='Null')
    objects = UserManager()

    USERNAME_FIELD = "email"