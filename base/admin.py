from django.contrib import admin


from .models import BairroBase, MunicipioBase, EstadoBase


@admin.register(BairroBase)
class BairroBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "municipio"]
    search_fields = ["descricao", "municipio"]


@admin.register(MunicipioBase)
class CidadeBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "estado"]
    search_fields = ["descricao", "estado"]


@admin.register(EstadoBase)
class EstadoBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "sigla"]
    search_fields = ["descricao", "sigla"]
