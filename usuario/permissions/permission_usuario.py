from enum import Enum
from django.contrib.contenttypes.models import ContentType


from ..models import Usuario


class PermissoesUsuario(Enum):
    VER = 'usuario_ver'
    EDITAR = 'usuario_editar'
    EXCLUIR = 'usuario_excluir'
    CADASTRAR = 'usuario_cadastrar'

    @property
    def content_type(self):
        return ContentType.objects.get_for_model(Usuario)


def get_permissoes_usuario_admin():
    return [
        {
            "codename": PermissoesUsuario.VER.value,
            "content_type": PermissoesUsuario.VER.content_type,
        },
        {
            "codename": PermissoesUsuario.EDITAR.value,
            "content_type": PermissoesUsuario.EDITAR.content_type,
        },
        {
            "codename": PermissoesUsuario.EXCLUIR.value,
            "content_type": PermissoesUsuario.EXCLUIR.content_type,
        },
        {
            "codename": PermissoesUsuario.CADASTRAR.value,
            "content_type": PermissoesUsuario.CADASTRAR.content_type,
        },
    ]


def get_permissoes_usuario_gerente():
    return [
        {
            "codename": PermissoesUsuario.VER.value,
            "content_type": PermissoesUsuario.VER.content_type,
        },
        {
            "codename": PermissoesUsuario.EDITAR.value,
            "content_type": PermissoesUsuario.EDITAR.content_type,
        },
        {
            "codename": PermissoesUsuario.CADASTRAR.value,
            "content_type": PermissoesUsuario.CADASTRAR.content_type,
        },
    ]


def get_permissoes_usuario_cliente():
    return [
        {
            "codename": PermissoesUsuario.VER.value,
            "content_type": PermissoesUsuario.VER.content_type,
        },
        {
            "codename": PermissoesUsuario.EDITAR.value,
            "content_type": PermissoesUsuario.EDITAR.content_type,
        },
    ]
