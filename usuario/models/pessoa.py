from django.db import models


from base.models.enderecobase import EnderecoBase


class Pessoa(EnderecoBase):
    nome = models.CharField(
        verbose_name="nome",
        max_length=255,
    )

    sobrenome = models.CharField(
        verbose_name="sobrenome",
        max_length=255,
    )

    cpf = models.CharField(
        verbose_name="cpf",
        unique=True,
        max_length=11,
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
        default_permissions = [] 

    def __str__(self):
        return f"{self.nome} - {self.sobrenome}"
