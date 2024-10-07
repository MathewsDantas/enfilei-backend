from ..constants import TipoUsuario
# from .permission_pedido import get_permissoes_pedido_garcom


def get_permissoes_garcom():
    return {
        TipoUsuario.GARCOM.value: [
            # -------------------- PEDIDO --------------------
            # get_permissoes_pedido_garcom(),
        ],
    }