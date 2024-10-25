from enum import Enum


class TipoSolicitacao(Enum):
    FAZER_PEDIDO = "fazer_pedido"
    CONVITE_USUARIO = "convite_usuario"

    @classmethod
    def values(self):
        return [item.value for item in TipoSolicitacao]


class StatusSolicitacao(Enum):
    CANCELADO = "cancelado"
    FINALIZADO = "finalizado"
    EM_ANALISE = "em_analise"

    @classmethod
    def values(self):
        return [item.value for item in StatusSolicitacao]
