from solicitacao.repository.solicitacao import SolicitacaoRepository


class SolicitacaoCase:
    def __init__(self):
        self.solicitacao_repository = SolicitacaoRepository()

    def criar_solicitacao(self, tipo, json, status=None):
        solicitacao = self.solicitacao_repository.create(
            tipo=tipo,
            json=json,
            status=status,
        )

        url = self.gerar_url_solicitacao(solicitacao)

        # Enviar email

    def gerar_url_solicitacao(self, solicitacao):
        return f"https://solicitacao.com/{solicitacao.id}"
