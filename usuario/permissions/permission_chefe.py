from ..constants import TipoUsuario
# from .permission_pedido import get_permissoes_pedido_chefe
# from .permission_produto import get_permissoes_produto_chefe


def get_permissoes_chefe():
    return {
        TipoUsuario.CHEFE.value: [
            # -------------------- PEDIDO --------------------
            # get_permissoes_pedido_chefe(),
            # -------------------- PRODUTO --------------------
            # get_permissoes_produto_chefe(),
        ],
    }
