from enum import Enum
from django.contrib.contenttypes.models import ContentType


from ..models import Solicitacao


class PermissoesSolicitacao(Enum):
    VER = "solicitacao_ver"
    EDITAR = "solicitacao_editar"
    EXCLUIR = "solicitacao_excluir"
    CADASTRAR = "solicitacao_cadastrar"
    APROVAR = "solicitacao_aprovar"
    REPROVAR = "solicitacao_reprovar"

    @classmethod
    def content_type(self):
        return ContentType.objects.get_for_model(Solicitacao)

    @property
    def name(self):
        return self.value


def get_permissoes_solicitacao(*permissoes: PermissoesSolicitacao):
    return [
        {
            "codename": permissao.value,
            "content_type": PermissoesSolicitacao.content_type(),
            "name": permissao.name,
        }
        for permissao in permissoes
    ]


def get_permissoes_solicitacao_admin():
    return get_permissoes_solicitacao(
        PermissoesSolicitacao.VER,
        PermissoesSolicitacao.EDITAR,
        PermissoesSolicitacao.EXCLUIR,
        PermissoesSolicitacao.CADASTRAR,
        PermissoesSolicitacao.APROVAR,
        PermissoesSolicitacao.REPROVAR,
    )
