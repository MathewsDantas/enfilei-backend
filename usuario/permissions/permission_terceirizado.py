from ..constants import TipoUsuario
from pedido.permissions.permission_pedido import get_permissoes_pedido_terceirizado


def get_permissoes_terceirizado():
    return {
        TipoUsuario.TERCEIRIZADO.value: [
            # -------------------- PEDIDO --------------------
            *get_permissoes_pedido_terceirizado(),
        ],
    }