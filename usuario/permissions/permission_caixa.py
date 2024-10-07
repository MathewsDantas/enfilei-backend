from ..constants import TipoUsuario
# from .permission_pedido import get_permissoes_pedido_caixa


def get_permissoes_caixa():
    return {
        TipoUsuario.CAIXA.value: [
            # -------------------- PEDIDO --------------------
            # get_permissoes_pedido_caixa(),
        ],
    }