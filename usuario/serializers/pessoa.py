from rest_framework import serializers
from usuario.models import Pessoa


class PessoaListSerializer(serializers.ModelSerializer):
    usuario_email = serializers.SerializerMethodField()
    usuario_id = serializers.SerializerMethodField()
    usuario_is_active = serializers.SerializerMethodField()

    class Meta:
        model = Pessoa
        fields = [
            "id",
            "nome_completo",
            "sobrenome",
            "cpf",
            "data_nacimento",
            "telefone",
            "cep",
            "usuario_email",
            "usuario_id",
            "usuario_is_active",
        ]

    def get_usuario_email(self, obj):
        return obj.usuario.email if obj.usuario else None

    def get_usuario_id(self, obj):
        return obj.usuario.id if obj.usuario else None

    def get_usuario_is_active(self, obj):
        return obj.usuario.is_active if obj.usuario else None
