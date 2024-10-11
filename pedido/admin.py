from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models.pedido import Pedido


class PedidoResource(resources.ModelResource):  # serve para importar e exportar dados
    class Meta:
        model = Pedido
        fields = ("id", "interno", "feito_por", "data", "status", "valor_total")


@admin.register(Pedido)
class PedidoAdmin(ImportExportModelAdmin):
    resource_class = PedidoResource
    list_display = ["id", "interno", "feito_por", "data", "status", "valor_total"]
    search_fields = ["feito_por", "status"]
    list_filter = ["status"]
