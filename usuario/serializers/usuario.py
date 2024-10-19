from rest_framework import serializers
from django.db import transaction


from usuario.models import Usuario, Pessoa
from usuario.repository import UsuarioRepository


class PessoaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            "nome_completo",
            "sobrenome",
            "cpf",
            "data_nacimento",
            "telefone",
            "cep",
        ]


class UsuarioCreateSerializer(serializers.ModelSerializer):
    pessoa = PessoaCreateSerializer()

    class Meta:
        model = Usuario
        fields = [
            "pessoa",
            "email",
            "password",
        ]

    def validate(self, data):

        return data

    @transaction.atomic
    def create(self, validated_data):
        pessoa_criada = Pessoa.objects.create(
            nome=validated_data["pessoa"]["nome_completo"],
            sobrenome=validated_data["pessoa"]["sobrenome"],
            cpf=validated_data["pessoa"]["cpf"],
            data_nacimento=validated_data["pessoa"]["data_nacimento"],
            telefone=validated_data["pessoa"]["telefone"],
            cep=validated_data["pessoa"]["cep"],
        )

        usuario = UsuarioRepository().create(
            email=validated_data["email"],
            password=validated_data["password"],
            pessoa=pessoa_criada,
        )

        return usuario
