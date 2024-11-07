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
            raise serializers.ValidationError({"cpf": "CPF já cadastrado"})

        if usuario_repository.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email já cadastrado"})

        if grupo not in TipoUsuario.names():
            raise serializers.ValidationError({"grupo": "Grupo inválido"})

        if solicitacao_repository.filter(
            json__email=email, status=StatusSolicitacao.EM_ANALISE.name
        ).exists():
            raise serializers.ValidationError(
                {"email": "Já existe uma solicitação em análise para esse email"}
            )

        if solicitacao_repository.filter(
            json__cpf=cpf, status=StatusSolicitacao.EM_ANALISE.name
        ).exists():
            raise serializers.ValidationError(
                {"cpf": "Já existe uma solicitação em análise para esse cpf"}
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
        solicitacao_case.criar_solicitacao_convite_usuario(
            tipo=TipoSolicitacao.CONVITE_USUARIO.name,
            json={
                "email": validated_data["email"],
                "cpf": validated_data["cpf"],
                "grupo": validated_data["grupo"],
            },
        )

        return validated_data


class SolicitacaoGetSerializer(serializers.ModelSerializer):
    status_value = serializers.SerializerMethodField()
    tipo_value = serializers.SerializerMethodField()

    class Meta:
        model = Solicitacao
        fields = [
            "id",
            "status",
            "tipo",
            "status_value",
            "tipo_value",
            "json",
        ]

    def get_status_value(self, obj):
        return obj.get_status_display()

    def get_tipo_value(self, obj):
        return obj.get_tipo_display()


class SolicitacaoEnviarEsqueciSenha(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    cpf = serializers.CharField(required=True)

    class Meta:
        model = Solicitacao
        fields = [
            "email",
            "cpf",
        ]

    def validate(self, data):
        email = data.get("email")
        cpf = data.get("cpf")

        usuario_repository = UsuarioRepository()
        solicitacao_repository = SolicitacaoRepository()

        if not usuario_repository.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email não cadastrado"})

        if solicitacao_repository.filter(
            json__email=email,
            status=StatusSolicitacao.EM_ANALISE.name,
            tipo=TipoSolicitacao.RESETAR_SENHA.name,
        ).exists():
            raise serializers.ValidationError(
                {
                    "email": "Já existe uma solicitação de resetar senha em análise para esse email"  # noqa
                }
            )

        if not usuario_repository.filter(pessoa__cpf=cpf).exists():
            raise serializers.ValidationError({"cpf": "CPF não cadastrado"})

        if not usuario_repository.filter(email=email, pessoa__cpf=cpf).exists():
            raise serializers.ValidationError(
                {"email": "Email e CPF não correspondem a um mesmo usuário"}
            )

        return data

    @transaction.atomic
    def create(self, validated_data):
        solicitacao_case = SolicitacaoCase()
        solicitacao_case.criar_solicitacao_resetar_senha(
            tipo=TipoSolicitacao.RESETAR_SENHA.name,
            json={
                "email": validated_data["email"],
                "cpf": validated_data["cpf"],
            },
        )

        return validated_data
