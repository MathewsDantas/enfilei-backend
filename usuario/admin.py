from django.contrib import admin


from .models import Usuario, Pessoa


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "is_active", "is_staff", "is_superuser"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["email"]


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "sobrenome", "telefone"]
    search_fields = ["nome", "telefone"]
