from django.db import models


from base.models.bairroBase import BairroBase
from base.models.municipioBase import MunicipioBase
from base.models.estadoBase import EstadoBase


class EnderecoBase(models.Model):
    cep = models.CharField(
        verbose_name="cep",
        max_length=9,
    )

    logradouro = models.CharField(
        verbose_name="logradouro",
        max_length=500,
    )

    numero = models.CharField(
        verbose_name="numero",
        max_length=10,
    )

    complemento = models.CharField(
        verbose_name="complemento",
        max_length=500,
        blank=True,
        null=True,
    )

    bairro = models.ForeignKey(
        verbose_name="bairro",
        to=BairroBase,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    municipio = models.ForeignKey(
        verbose_name="municipio",
        to=MunicipioBase,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    estado = models.ForeignKey(
        verbose_name="estado",
        to=EstadoBase,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def cep_formatado(self):
        if self.cep:
            return f"{self.cep[:5]}-{self.cep[5:]}"

    class Meta:
        abstract = True

    def __str__(self):
        return (
            f"{self.cep} - {self.logradouro} - {self.numero} - "
            f"{self.complemento} - {self.bairro} - {self.cidade} - "
            f"{self.estado}"
        )
