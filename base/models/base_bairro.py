from django.db import models

from base.models.base_municipio import BaseMunicipio
from base.models.base_estado import BaseEstado


class BaseBairro(models.Model):
    descricao = models.CharField(
        verbose_name="descricao",
        max_length=255,
    )

    municipio = models.ForeignKey(
        verbose_name="municipio",
        to=BaseMunicipio,
        on_delete=models.CASCADE,
    )

    estado = models.ForeignKey(
        verbose_name="estado",
        to=BaseEstado,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "base_bairro"

    def __str__(self):
        return f"{self.descricao} - {self.municipio}"
