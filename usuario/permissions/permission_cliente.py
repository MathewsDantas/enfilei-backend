from ..constants import TipoUsuario
from pedido.permissions.permission_pedido import get_permissoes_pedido_cliente
from .permission_usuario import get_permissoes_usuario_cliente


def get_permissoes_cliente():
    return {
        TipoUsuario.CLIENTE.value: [
            # -------------------- PEDIDO --------------------
            *get_permissoes_pedido_cliente(),
            # -------------------- USUARIO --------------------
            *get_permissoes_usuario_cliente(),
        ],
    }