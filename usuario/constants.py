from enum import Enum


class TipoUsuario(Enum):
    ADMIN = "Admin"
    GERENTE = "Gerente"
    GARCOM = "Garçom"
    COZINHEIRO = "Cozinheiro"
    CAIXA = "Caixa"
    TERCEIRIZADO = "Terceirizado"

    CLIENTE = "Cliente"

    @classmethod
    def is_interno(self):
        return self in [
            TipoUsuario.GARCOM,
            TipoUsuario.COZINHEIRO,
            TipoUsuario.GERENTE,
            TipoUsuario.CAIXA,
            TipoUsuario.ADMIN,
        ]
