from django.db import models

from base.models.cidadeBase import CidadeBase
from base.models.estadoBase import EstadoBase


class BairroBase(models.Model):
    descricao = models.CharField(
        verbose_name="descricao",
        max_length=255,
    )

    cidade = models.ForeignKey(
        verbose_name="cidade",
        to=CidadeBase,
        on_delete=models.CASCADE,
    )

    estado = models.ForeignKey(
        verbose_name="estado",
        to=EstadoBase,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "bairro_base"

    def __str__(self):
        return f"{self.descricao} - {self.cidade}"