from rest_framework import serializers
from django.db import transaction


from base.utils.validate_documentos import validate_cpf
from usuario.constants import TipoUsuario
from usuario.repository import UsuarioRepository
from solicitacao.models import Solicitacao
from solicitacao.constants import TipoSolicitacao, StatusSolicitacao
from solicitacao.cases import SolicitacaoCase
from solicitacao.repository import SolicitacaoRepository


class SolicitacaoCreateConviteSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    cpf = serializers.CharField(required=True)
    grupo = serializers.ChoiceField(required=True, choices=TipoUsuario.names_values())

    def validate(self, data):
        cpf = data.get("cpf")
        grupo = data.get("grupo")
        email = data.get("email")

        usuario_repository = UsuarioRepository()
        solicitacao_repository = SolicitacaoRepository()

        validate_cpf(cpf)

        if usuario_repository.filter(pessoa__cpf=cpf).exists():
            raise serializers.ValidationError("CPF já cadastrado")

        if usuario_repository.filter(email=email).exists():
            raise serializers.ValidationError("Email já cadastrado")

        if grupo not in TipoUsuario.names():
            raise serializers.ValidationError("Grupo inválido")

        if solicitacao_repository.filter(
            json__email=email, status=StatusSolicitacao.EM_ANALISE.value
        ).exists():
            raise serializers.ValidationError(
                "Já existe uma solicitação em análise para esse email"
            )

        if solicitacao_repository.filter(
            json__cpf=cpf, status=StatusSolicitacao.EM_ANALISE.value
        ).exists():
            raise serializers.ValidationError(
                "Já existe uma solicitação em análise para esse CPF"
            )

        return data

    class Meta:
        model = Solicitacao
        fields = [
            "email",
            "cpf",
            "grupo",
        ]

    @transaction.atomic
    def create(self, validated_data):
        solicitacao_case = SolicitacaoCase()
        solicitacao_case.criar_solicitacao(
            tipo=TipoSolicitacao.CONVITE_USUARIO.value,
            json={
                "email": validated_data["email"],
                "cpf": validated_data["cpf"],
                "grupo": validated_data["grupo"],
            },
        )

        return validated_data


class SolicitacaoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = "__all__"


class SolicitacaoCreateNovoUsuarioSerializer(serializers.ModelSerializer):
    pass
