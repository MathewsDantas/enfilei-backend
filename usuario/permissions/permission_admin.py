from ..constants import TipoUsuario
from .permission_usuario import get_permissoes_usuario_admin
from pedido.permissions.permission_pedido import get_permissoes_pedido_admin


def get_permissoes_admin():
    return {
        TipoUsuario.ADMIN.value: [
            # -------------------- PEDIDO --------------------
            *get_permissoes_pedido_admin(),
            # -------------------- USUARIO --------------------
            *get_permissoes_usuario_admin(),
        ],
    }