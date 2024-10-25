from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)

from solicitacao.models import Solicitacao
from solicitacao.serializers import (
    SolicitacaoCreateConviteSerializer,
    SolicitacaoGetSerializer,
)


@extend_schema_view(
    create=extend_schema(
        exclude=True,
    ),
    list=extend_schema(
        tags=["solicitacao"],
        summary="Listar solicitações",
    ),
    retrieve=extend_schema(
        tags=["solicitacao"],
        summary="Detalhar uma solicitação",
    ),
    destroy=extend_schema(
        tags=["solicitacao"],
        summary="Deletar uma solicitação",
    ),
    criar_convite_usuario=extend_schema(
        tags=["usuario"],
        summary="Criar solicitação de convite para um usuário",
    ),
)
class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.all()
    http_method_names = ["get", "delete", "post"]

    def get_serializer_class(self):
        if self.action == "criar_convite_usuario":
            return SolicitacaoCreateConviteSerializer
        return SolicitacaoGetSerializer

    @action(detail=False, methods=["post"])
    def criar_convite_usuario(self, request, pk=None):
        serializer = SolicitacaoCreateConviteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
