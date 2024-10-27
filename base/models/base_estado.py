from django.db import models


class BaseEstado(models.Model):
    descricao = models.CharField(
        verbose_name="descricao",
        max_length=255,
    )

    sigla = models.CharField(
        verbose_name="sigla",
        max_length=2,
    )

    class Meta:
        db_table = "base_estado"

    def __str__(self):
        return f"{self.descricao} - {self.sigla}"
