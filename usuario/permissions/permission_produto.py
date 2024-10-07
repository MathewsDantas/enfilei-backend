from enum import Enum


class PermissoesProduto(Enum):
    VER = "produto_ver"
    EDITAR = "produto_editar"
    EXCLUIR = "produto_excluir"
    CADASTRAR = "produto_cadastrar"

    @property
    def content_type(self):
        return None


def get_permissoes_produto_admin():
    return (
        {
            "codename": PermissoesProduto.VER.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.EDITAR.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.EXCLUIR.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.CADASTRAR.value,
            "content_type": PermissoesProduto.content_type,
        },
    )


def get_permissoes_produto_gerente():
    return (
        {
            "codename": PermissoesProduto.VER.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.EDITAR.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.EXCLUIR.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.CADASTRAR.value,
            "content_type": PermissoesProduto.content_type,
        },
    )


def get_permissoes_produto_chefe():
    return (
        {
            "codename": PermissoesProduto.VER.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.EDITAR.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.EXCLUIR.value,
            "content_type": PermissoesProduto.content_type,
        },
        {
            "codename": PermissoesProduto.CADASTRAR.value,
            "content_type": PermissoesProduto.content_type,
        },
    )
