from django.db import models


from .constants import TipoSolicitacao, StatusSolicitacao


class Solicitacao(models.Model):
    tipo = models.CharField(
        verbose_name="tipo",
        max_length=255,
        choices=[(tag.value, tag.name) for tag in TipoSolicitacao],
    )

    status = models.CharField(
        verbose_name="status",
        max_length=255,
        default=StatusSolicitacao.EM_ANALISE.value,
        choices=[(tag.value, tag.name) for tag in StatusSolicitacao],
    )

    json = models.JSONField(
        verbose_name="json",
    )

    class Meta:
        verbose_name = "Solicitação"
        db_table = "solicitacao"
        default_permissions = []

    def __str__(self):
        return f"{self.tipo} - {self.status} - {self.data_expiracao}"
