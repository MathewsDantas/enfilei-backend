from django.db import models


from usuario.models.usuario import Usuario
from base.models.base_model import BaseModel


class Pedido(BaseModel):

    status = models.CharField(
        verbose_name="status",
        max_length=255,
    )

    data = models.DateField(
        verbose_name="data",
    )

    valor_total = models.DecimalField(
        verbose_name="valor total",
        max_digits=10,
        decimal_places=2,
    )

    feito_por = models.ForeignKey(
        verbose_name="feito por",
        to=Usuario,
        on_delete=models.CASCADE,
    )

    interno = models.BooleanField(
        verbose_name="interno",
        default=False,
        null=False,
        blank=False,
    )

    # Executado antes de salvar o objeto no banco de dados
    def clean(self):
        if self.valor_total < 0:
            raise ValueError("O valor total do pedido não pode ser negativo")

    class Meta:
        db_table = "pedido"
        default_permissions = []
        indexes = [
            models.Index(fields=["data"]),
            models.Index(fields=["feito_por"]),
        ]

    def __str__(self):
        return f"{self.data} - {self.valor_total}"
