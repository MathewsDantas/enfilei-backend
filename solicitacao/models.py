from django.db import models


from .constants import TipoSolicitacao


class Solicitacao(models.Model):
    tipo = models.CharField(
        verbose_name="tipo",
        max_length=255,
        choices=[(tag.name, tag.value) for tag in TipoSolicitacao],
    )

    data_expiracao = models.DateTimeField(
        verbose_name="data_expiracao",
    )

    json = models.JSONField(
        verbose_name="json",
    )

    class Meta:
        verbose_name = "Solicitação"
        db_table = "solicitacao"
        default_permissions = []

    def __str__(self):
        return f"{self.tipo} - {self.data_expiracao}"
