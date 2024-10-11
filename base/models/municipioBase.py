from django.db import models

from base.models.estadoBase import EstadoBase


class MunicipioBase(models.Model):
    descricao = models.CharField(
        verbose_name="descricao",
        max_length=255,
    )

    estado = models.ForeignKey(
        verbose_name="estado",
        to=EstadoBase,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "municipio_base"

    def __str__(self):
        return f"{self.descricao} - {self.estado}"
