from rest_framework import serializers
from django.db import transaction


from solicitacao.repository.solicitacao import SolicitacaoRepository
from solicitacao.constants import StatusSolicitacao
from usuario.models import Usuario, Pessoa
from usuario.cases import UsuarioCase


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
    id_solicitacao = serializers.UUIDField(required=False)

    class Meta:
        model = Usuario
        fields = [
            "pessoa",
            "email",
            "password",
            "id_solicitacao",
        ]

    def validate(self, data):
        pessoa = data.get("pessoa")
        email = data.get("email")

        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email já cadastrado"})

        if Pessoa.objects.filter(cpf=pessoa["cpf"]).exists():
            raise serializers.ValidationError({"cpf": "CPF já cadastrado"})

        if Usuario.objects.filter(pessoa__cpf=pessoa["cpf"]).exists():
            raise serializers.ValidationError({"cpf": "CPF já cadastrado"})

        if data and data.get("id_solicitacao"):
            if not SolicitacaoRepository().filter(id=data["id_solicitacao"]).exists():
                raise serializers.ValidationError(
                    {"id_solicitacao": "Solicitação não encontrada"}
                )

        return data

    @transaction.atomic
    def create(self, validated_data):
        primeiro_nome = validated_data["pessoa"]["nome_completo"].split(" ")[0]
        sobre_nome = " ".join(validated_data["pessoa"]["nome_completo"].split(" ")[1:])

        pessoa_criada = Pessoa.objects.create(
            nome_completo=validated_data["pessoa"]["nome_completo"],
            primeiro_nome=primeiro_nome,
            sobrenome=sobre_nome,
            cpf=validated_data["pessoa"]["cpf"],
            data_nacimento=validated_data["pessoa"]["data_nacimento"],
            telefone=validated_data["pessoa"]["telefone"],
            cep=validated_data["pessoa"]["cep"],
        )

        usuario = UsuarioCase().criar_usuario_inativo(
            email=validated_data["email"],
            password=validated_data["password"],
            pessoa=pessoa_criada,
        )

        if validated_data.get("id_solicitacao"):
            solicitacao = SolicitacaoRepository().get_by_id(
                validated_data["id_solicitacao"]
            )
            solicitacao.json["id_usuario_criado"] = str(usuario.id)
            solicitacao.status = StatusSolicitacao.FINALIZADO.value
            solicitacao.save()

        return usuario


class UsuarioListSerializer(serializers.ModelSerializer):
    nome_completo = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = [
            "id",
            "nome_completo",
            "email",
            "is_active",
        ]

    def get_nome_completo(self, obj):
        return obj.pessoa.nome_completo if obj.pessoa else None


class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "email",
            "password",
            "is_active",
        ]

    def validate(self, data):
        email = data.get("email")

        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email já cadastrado"})

        return data

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.is_active = validated_data.get("is_active", instance.is_active)

        password = validated_data.get("password", instance.password)
        if password:
            instance.set_password(password)

        instance.save()

        return instance

    def to_representation(self, instance):

        return UsuarioListSerializer(instance).to_representation(instance)
