from django.db import models


from .constants import TipoSolicitacao, StatusSolicitacao
from base.models.base_model import BaseModel


class Solicitacao(BaseModel):
    tipo = models.CharField(
        verbose_name="tipo",
        max_length=255,
        choices=[(tag.name, tag.value) for tag in TipoSolicitacao],
    )

    status = models.CharField(
        verbose_name="status",
        max_length=255,
        default=StatusSolicitacao.EM_ANALISE.name,
        choices=[(tag.name, tag.value) for tag in StatusSolicitacao],
    )

    json = models.JSONField(
        verbose_name="json",
    )

    data_criacao = models.DateTimeField(
        verbose_name="dataCriacao",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Solicitação"
        db_table = "solicitacao"
        default_permissions = []

    def __str__(self):
        return f"{self.tipo} - {self.status}"
