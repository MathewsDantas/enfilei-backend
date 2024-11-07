import os
from django.core.mail import send_mail
from base.utils.urls_config import Frontend
from uuid import UUID

from solicitacao.repository.solicitacao import SolicitacaoRepository


class SolicitacaoCase:
    def __init__(self):
        self.solicitacao_repository = SolicitacaoRepository()
        self.from_email = os.environ.get("EMAIL_HOST_USER")

    def criar_solicitacao_convite_usuario(self, tipo, json):
        solicitacao = self.solicitacao_repository.create(
            tipo=tipo,
            json=json,
        )

        url = self.gerar_url_solicitacao(solicitacao.id, "convite_usuario")
        send_mail(
            subject="Enfilei - Convite para cadastro",
            message=f"Olá, você foi convidado para se cadastrar no Enfilei, clique no link para se cadastrar: {url}",  # noqa
            from_email=self.from_email,
            recipient_list=[json["email"]],
            html_message=f"Olá, você foi convidado para se cadastrar no Enfilei, clique no link para se cadastrar: <a href='{url}'>Cadastrar</a>",  # noqa
        )

    def criar_solicitacao_resetar_senha(self, tipo, json):
        solicitacao = self.solicitacao_repository.create(
            tipo=tipo,
            json=json,
        )

        url = self.gerar_url_solicitacao(solicitacao.id, "resetar_senha")
        send_mail(
            subject="Enfilei - Resetar senha",
            message=f"Olá, você solicitou a alteração de senha, clique no link para alterar sua senha: {url}",  # noqa
            from_email=self.from_email,
            recipient_list=[json["email"]],
            html_message=f"Olá, você solicitou a alteração de senha, clique no link para alterar sua senha: <a href='{url}'>Alterar senha</a>",  # noqa
        )

    def gerar_url_solicitacao(self, solicitacao_id: UUID, tipo: str) -> str:
        if tipo == "convite_usuario":
            return Frontend.CONVIDAR_USUARIO.value.format(solicitacao_id=solicitacao_id)
        elif tipo == "resetar_senha":
            return Frontend.RESETAR_SENHA.value.format(solicitacao_id=solicitacao_id)
        else:
            raise ValueError(f"Tipo de solicitação desconhecido: {tipo}")
