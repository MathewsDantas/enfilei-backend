from django.contrib import admin


from .models import BairroBase, CidadeBase, EstadoBase


@admin.register(BairroBase)
class BairroBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "cidade"]
    search_fields = ["descricao", "cidade"]


@admin.register(CidadeBase)
class CidadeBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "estado"]
    search_fields = ["descricao", "estado"]


@admin.register(EstadoBase)
class EstadoBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "sigla"]
    search_fields = ["descricao", "sigla"]
