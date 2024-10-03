from django.contrib import admin


from .models import BairroBase, CidadeBase, EnderecoBase, EstadoBase


@admin.register(BairroBase)
class BairroBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "cidade"]
    search_fields = ["descricao", "cidade"]


@admin.register(CidadeBase)
class CidadeBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "estado"]
    search_fields = ["descricao", "estado"]


@admin.register(EnderecoBase)
class EnderecoBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "logradouro", "numero", "bairro"]
    search_fields = ["logradouro", "numero", "bairro"]


@admin.register(EstadoBase)
class EstadoBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "descricao", "sigla"]
    search_fields = ["descricao", "sigla"]
