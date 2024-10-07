from enum import Enum


class TipoUsuario(Enum):
    ADMIN = "Admin"
    GERENTE = "Gerente"
    CHEFE = "Chefe"
    GARCOM = "Garçom"
    COZINHEIRO = "Cozinheiro"
    CAIXA = "Caixa"
    TERCEIRIZADO = "Terceirizado"

    CLIENTE = "Cliente"

    @property
    def is_interno(self):
        return self in [
            TipoUsuario.GARCOM,
            TipoUsuario.COZINHEIRO,
            TipoUsuario.GERENTE,
            TipoUsuario.CAIXA,
            TipoUsuario.CHEFE,
            TipoUsuario.ADMIN,
        ]
