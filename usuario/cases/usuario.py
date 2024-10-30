import os
from django.core.mail import send_mail
from uuid import UUID


from base.utils.urls_config import Frontend
from usuario.repository.usuario import UsuarioRepository
from usuario.models import Usuario, Pessoa


class UsuarioCase:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        self.from_email = os.environ.get("EMAIL_HOST_USER")

    def criar_usuario_inativo(
        self, email: str, password: str, pessoa: Pessoa
    ) -> Usuario:
        usuario = self.usuario_repository.create(
            email=email,
            password=password,
            pessoa=pessoa,
            is_active=False,
        )

        url = self.gerar_url_confirmacao_usuario(usuario.id)

        send_mail(
            subject="Enfilei - Confirmação de cadastro",
            message=f"Olá, você foi cadastrado no Enfilei, clique no link para confirmar o cadastro: {url}",  # noqa
            from_email=self.from_email,
            recipient_list=[email],
            html_message=f"Olá, você foi cadastrado no Enfilei, clique no link para confirmar o cadastro: <a href='{url}'>Confirmar</a>",  # noqa
        )

        return usuario

    def gerar_url_confirmacao_usuario(self, usuario_id: UUID) -> str:
        return Frontend.CONFIRMAR_USUARIO.value.format(usuario_id=usuario_id)
