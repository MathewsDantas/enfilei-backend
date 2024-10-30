import os
from django.core.mail import send_mail
from base.utils.urls_config import Frontend
from uuid import UUID

from solicitacao.repository.solicitacao import SolicitacaoRepository


class SolicitacaoCase:
    def __init__(self):
        self.solicitacao_repository = SolicitacaoRepository()
        self.from_email = os.environ.get("EMAIL_HOST_USER")

    def criar_solicitacao(self, tipo, json):
        solicitacao = self.solicitacao_repository.create(
            tipo=tipo,
            json=json,
        )

        url = self.gerar_url_solicitacao(solicitacao.id)
        send_mail(
            subject="Enfilei - Convite para cadastro",
            message=f"Olá, você foi convidado para se cadastrar no Enfilei, clique no link para se cadastrar: {url}",  # noqa
            from_email=self.from_email,
            recipient_list=[json["email"]],
            html_message=f"Olá, você foi convidado para se cadastrar no Enfilei, clique no link para se cadastrar: <a href='{url}'>Cadastrar</a>",  # noqa
        )

    def gerar_url_solicitacao(
        self,
        solicitacao_id: UUID,
    ):
        return Frontend.CONVIDAR_USUARIO.value.format(solicitacao_id=solicitacao_id)
