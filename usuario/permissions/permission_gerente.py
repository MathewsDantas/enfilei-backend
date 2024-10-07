from ..constants import TipoUsuario
# from .permission_pedido import get_permissoes_pedido_gerente
# from .permission_produto import get_permissoes_produto_gerente
from .permission_usuario import get_permissoes_usuario_gerente


def get_permissoes_gerente():
    return {
        TipoUsuario.GERENTE.value: [
            # -------------------- PEDIDO --------------------
            # get_permissoes_pedido_gerente(),
            # -------------------- USUARIO --------------------
            *get_permissoes_usuario_gerente(),
            # -------------------- PRODUTO --------------------
            # get_permissoes_produto_gerente(),
        ],
    }