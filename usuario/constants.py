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
    def values(self):
        return [item.value for item in TipoUsuario]

    @classmethod
    def names(self):
        return [item.name for item in TipoUsuario]

    @classmethod
    def names_values(self):
        return [(item.name, item.value) for item in TipoUsuario]

    @classmethod
    def is_interno(self):
        return self in [
            TipoUsuario.GARCOM,
            TipoUsuario.COZINHEIRO,
            TipoUsuario.GERENTE,
            TipoUsuario.CAIXA,
            TipoUsuario.ADMIN,
        ]
