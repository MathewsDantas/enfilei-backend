from django.contrib import admin
from import_export import resources


from .models.pedido import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id", "interno", "feito_por", "data", "status", "valor_total"]
    search_fields = ["feito_por", "status"]
    list_filter = ["status"]


class PedidoResource(resources.ModelResource):
    class Meta:
        model = Pedido
