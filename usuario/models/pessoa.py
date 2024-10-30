from django.db import models


from base.models.base_endereco import BaseEndereco
from base.utils import validate_documentos


class Pessoa(BaseEndereco):
    nome_completo = models.CharField(
        verbose_name="nome_completo",
        max_length=255,
    )

    primeiro_nome = models.CharField(
        verbose_name="primeiro_nome",
        max_length=255,
    )

    sobrenome = models.CharField(
        verbose_name="sobrenome",
        max_length=255,
    )

    cpf = models.CharField(
        verbose_name="cpf",
        unique=True,
        max_length=14,
        validators=[
            validate_documentos.validate_cpf,
        ],
    )

    data_nacimento = models.DateField(
        verbose_name="data_nacimento",
    )

    telefone = models.CharField(
        verbose_name="telefone",
        max_length=11,
    )

    class Meta:
        db_table = "pessoa"
        default_permissions = []  # Serve para não criar permissões automaticamente

    def __str__(self):
        return f"{self.nome_completo} - {self.sobrenome}"
