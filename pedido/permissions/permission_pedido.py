from enum import Enum
from django.contrib.contenttypes.models import ContentType


from ..models.pedido import Pedido


class PermissoesPedido(Enum):
    VER = 'pedido_ver'
    EDITAR = 'pedido_editar'
    EXCLUIR = 'pedido_excluir'
    CADASTRAR = 'pedido_cadastrar'
    PAGAR = 'pedido_pagar'
    AVALIAR = 'pedido_avaliar'
    CANCELAR = 'pedido_cancelar'

    @classmethod
    def content_type(self):
        return ContentType.objects.get_for_model(Pedido)


def get_permissoes_pedido_admin():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EDITAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EXCLUIR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CADASTRAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.PAGAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.AVALIAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CANCELAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )


def get_permissoes_pedido_gerente():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EDITAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EXCLUIR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CADASTRAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.PAGAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.AVALIAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CANCELAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )


def get_permissoes_pedido_chefe():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EDITAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EXCLUIR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CADASTRAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.AVALIAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CANCELAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )


def get_permissoes_pedido_caixa():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EDITAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EXCLUIR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CADASTRAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.PAGAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.AVALIAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CANCELAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )


def get_permissoes_pedido_garcom():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EDITAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EXCLUIR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CADASTRAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.PAGAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.AVALIAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CANCELAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )


def get_permissoes_pedido_cozinheiro():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EDITAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )


def get_permissoes_pedido_terceirizado():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )


def get_permissoes_pedido_cliente():
    return (
        {
            "codename": PermissoesPedido.VER.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.EDITAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CADASTRAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.PAGAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.AVALIAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
        {
            "codename": PermissoesPedido.CANCELAR.value,
            "content_type": PermissoesPedido.content_type(),
        },
    )
