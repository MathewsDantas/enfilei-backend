from django.db import models

from base.models.base_estado import BaseEstado


class BaseMunicipio(models.Model):
    descricao = models.CharField(
        verbose_name="descricao",
        max_length=255,
    )

    estado = models.ForeignKey(
        verbose_name="estado",
        to=BaseEstado,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "base_municipio"

    def __str__(self):
        return f"{self.descricao} - {self.estado}"
