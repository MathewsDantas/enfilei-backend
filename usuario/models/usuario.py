from uuid import uuid4

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from usuario.models.pessoa import Pessoa


def upload_to(instance, filename):
    uuid = str(uuid4()).replace("-", "")
    return f"avatar/{instance.username}/{uuid}.{filename}"


class Usuario(AbstractUser):

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

    groups = models.ManyToManyField(
        verbose_name="groups",
        to=Group,
        related_name="usuario_usuario",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        verbose_name="userPermissions",
        to=Permission,
        related_name="usuario_permissions",
        blank=True,
    )

    def get_avatar(self):
        if self.avatar_img:
            return self.avatar_img.url
        return None

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "usuario"

    def __str__(self):
        return f"{self.username} - {self.email} - {self.pessoa}"
