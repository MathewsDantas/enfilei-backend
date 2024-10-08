from ..constants import TipoUsuario
from pedido.permissions.permission_pedido import get_permissoes_pedido_cozinheiro


def get_permissoes_cozinheiro():
    return {
        TipoUsuario.COZINHEIRO.value: [
            # -------------------- PEDIDO --------------------
            *get_permissoes_pedido_cozinheiro(),
        ],
    }
