from django.contrib import admin


from .models import BaseBairro, BaseMunicipio, BaseEstado


@admin.register(BaseBairro)
class BairroBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "municipio"]
    search_fields = ["descricao", "municipio"]


@admin.register(BaseMunicipio)
class CidadeBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "estado"]
    search_fields = ["descricao", "estado"]


@admin.register(BaseEstado)
class EstadoBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "sigla"]
    search_fields = ["descricao", "sigla"]
