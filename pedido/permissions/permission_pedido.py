from enum import Enum
from typing import List, Dict
from django.contrib.contenttypes.models import ContentType


from ..models.pedido import Pedido


class PermissoesPedido(Enum):
    VER = "pedido_ver"
    EDITAR = "pedido_editar"
    EXCLUIR = "pedido_excluir"
    CADASTRAR = "pedido_cadastrar"
    PAGAR = "pedido_pagar"
    AVALIAR = "pedido_avaliar"
    CANCELAR = "pedido_cancelar"

    @classmethod
    def content_type(self):
        return ContentType.objects.get_for_model(Pedido)

    @property
    def name(self):
        return self.value


def get_permissoes_pedido(*permissoes: PermissoesPedido) -> List[Dict[str, str]]:
    return [
        {
            "codename": permissao.value,
            "content_type": PermissoesPedido.content_type(),
            "name": permissao.name,
        }
        for permissao in permissoes
    ]


def get_permissoes_pedido_admin():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
        PermissoesPedido.EDITAR,
        PermissoesPedido.EXCLUIR,
        PermissoesPedido.CADASTRAR,
        PermissoesPedido.PAGAR,
        PermissoesPedido.AVALIAR,
        PermissoesPedido.CANCELAR,
    )


def get_permissoes_pedido_gerente():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
        PermissoesPedido.EDITAR,
        PermissoesPedido.EXCLUIR,
        PermissoesPedido.CADASTRAR,
        PermissoesPedido.PAGAR,
        PermissoesPedido.AVALIAR,
        PermissoesPedido.CANCELAR,
    )


def get_permissoes_pedido_chefe():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
        PermissoesPedido.EDITAR,
        PermissoesPedido.EXCLUIR,
        PermissoesPedido.CADASTRAR,
        PermissoesPedido.AVALIAR,
        PermissoesPedido.CANCELAR,
    )


def get_permissoes_pedido_caixa():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
        PermissoesPedido.EDITAR,
        PermissoesPedido.EXCLUIR,
        PermissoesPedido.CADASTRAR,
        PermissoesPedido.PAGAR,
        PermissoesPedido.AVALIAR,
        PermissoesPedido.CANCELAR,
    )


def get_permissoes_pedido_garcom():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
        PermissoesPedido.EDITAR,
        PermissoesPedido.EXCLUIR,
        PermissoesPedido.CADASTRAR,
        PermissoesPedido.PAGAR,
        PermissoesPedido.AVALIAR,
        PermissoesPedido.CANCELAR,
    )


def get_permissoes_pedido_cozinheiro():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
        PermissoesPedido.EDITAR,
    )


def get_permissoes_pedido_terceirizado():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
    )


def get_permissoes_pedido_cliente():
    return get_permissoes_pedido(
        PermissoesPedido.VER,
        PermissoesPedido.EDITAR,
        PermissoesPedido.CADASTRAR,
        PermissoesPedido.PAGAR,
        PermissoesPedido.AVALIAR,
        PermissoesPedido.CANCELAR,
    )
