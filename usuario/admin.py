from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Usuario, Pessoa


class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario
        fields = ("id", "email", "is_active", "is_staff", "is_superuser")


@admin.register(Usuario)
class UsuarioAdmin(ImportExportModelAdmin):
    resource_class = UsuarioResource
    list_display = ["id", "email", "is_active", "is_staff", "is_superuser"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["email"]


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "sobrenome", "telefone"]
    search_fields = ["nome", "telefone"]
