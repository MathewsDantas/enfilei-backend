from enum import Enum
from project_enfilei.settings import FRONT_URL


class Frontend(Enum):
    HOST = FRONT_URL
    CONVIDAR_USUARIO = f'{HOST}/convite-usuario/{"{solicitacao_id}"}'
    CONFIRMAR_USUARIO = f'{HOST}/confirmar-usuario/{"{usuario_id}"}'
    RESETAR_SENHA = f'{HOST}/resetar-senha/{"{solicitacao_id}"}'
