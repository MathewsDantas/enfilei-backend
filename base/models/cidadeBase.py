from django.db import models

from base.models.estadoBase import EstadoBase


class CidadeBase(models.Model):
    descricao = models.CharField(
        verbose_name="descricao",
        max_length=255,
    )

    codigo_ibge = models.CharField(
        verbose_name="codigoibge",
        max_length=10,
    )

    estado = models.ForeignKey(
        verbose_name="estado",
        to=EstadoBase,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "cidade_base"

    def __str__(self):
        return f"{self.descricao} - {self.codigo_ibge} - {self.estado}"
