from enum import Enum


class TipoSolicitacao(Enum):
    FAZER_PEDIDO = "Fazer pedido"
    CONVITE_USUARIO = "Convite de usuário"

    @classmethod
    def values(self):
        return [item.value for item in TipoSolicitacao]


class StatusSolicitacao(Enum):
    CANCELADO = "Cancelado"
    FINALIZADO = "Finalizado"
    EM_ANALISE = "Em análise"

    @classmethod
    def values(self):
        return [item.value for item in StatusSolicitacao]
