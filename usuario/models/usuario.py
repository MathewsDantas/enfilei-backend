from uuid import uuid4
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils import timezone

from usuario.models.pessoa import Pessoa
from base.models.base_model import BaseModel


def upload_to(instance, filename):
    uuid = str(uuid4()).replace("-", "")
    return f"avatar/{instance.email}/{uuid}.{filename}"


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)  # se não existir, cria
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):  # Basicamente ele pega o email e faz a busca
        return self.get(email=email)


class Usuario(AbstractBaseUser, PermissionsMixin, BaseModel):

    objects = UsuarioManager()

    email = models.EmailField(
        verbose_name="email",
        unique=True,
        max_length=255,
    )

    aceita_lgpd = models.BooleanField(
        verbose_name="aceitalgpd",
        default=False,
        null=False,
        blank=False,
    )

    verificado = models.BooleanField(
        verbose_name="verificado",
        default=False,
        null=False,
        blank=False,
    )

    avatar_img = models.ImageField(
        verbose_name="avatarImg",
        upload_to=upload_to,
        null=True,
        blank=True,
    )

    pessoa = models.OneToOneField(
        verbose_name="pessoa",
        to=Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    def get_avatar(self):
        if self.avatar_img:
            return self.avatar_img.url
        return None

    USERNAME_FIELD = "email"  # campo que sera usado para fazer login

    class Meta:
        db_table = "usuario"
        default_permissions = []

    def __str__(self):
        return f"{self.email} - {self.pessoa}"
