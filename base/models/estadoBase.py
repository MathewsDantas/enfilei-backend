from django.db import models


class EstadoBase(models.Model):
    descricao = models.CharField(
        verbose_name="descricao",
        max_length=255,
    )

    codigo_ibge = models.CharField(
        verbose_name="codigoIBGE",
        max_length=2,
    )

    sigla = models.CharField(
        verbose_name="sigla",
        max_length=2,
    )

    class Meta:
        db_table = "estado_base"

    def __str__(self):
        return f"{self.descricao} - {self.sigla} - {self.codigoIBGE}"
