from enum import Enum
from typing import List, Dict
from django.contrib.contenttypes.models import ContentType


from ..models import Usuario


class PermissoesUsuario(Enum):
    VER = "usuario_ver"
    EDITAR = "usuario_editar"
    EXCLUIR = "usuario_excluir"
    CADASTRAR = "usuario_cadastrar"

    @classmethod
    def content_type(self):
        return ContentType.objects.get_for_model(Usuario)

    @property
    def name(self):
        return self.value


def get_permissoes_usuario(*permissoes: PermissoesUsuario) -> List[Dict[str, str]]:
    return [
        {
            "codename": permissao.value,
            "content_type": PermissoesUsuario.content_type(),
            "name": permissao.name,
        }
        for permissao in permissoes
    ]


def get_permissoes_usuario_admin():
    return get_permissoes_usuario(
        PermissoesUsuario.VER,
        PermissoesUsuario.EDITAR,
        PermissoesUsuario.EXCLUIR,
        PermissoesUsuario.CADASTRAR,
    )


def get_permissoes_usuario_gerente():
    return get_permissoes_usuario(
        PermissoesUsuario.VER,
        PermissoesUsuario.EDITAR,
        PermissoesUsuario.CADASTRAR,
    )


def get_permissoes_usuario_cliente():
    return get_permissoes_usuario(
        PermissoesUsuario.VER,
        PermissoesUsuario.EDITAR,
    )
