from enum import Enum
from project_enfilei.settings import FRONT_URL


class Frontend(Enum):
    HOST = FRONT_URL
    CONVIDAR_USUARIO = f'{HOST}/convite-usuario/{"{solicitacao_id}"}'
