from solicitacao.models import Solicitacao


class SolicitacaoRepository:
    def create(
        self,
        tipo: str,
        json: dict,
        status: str = None,
    ) -> Solicitacao:
        data = {
            "tipo": tipo,
            "json": json,
        }
        if status is not None:
            data["status"] = status

        return Solicitacao.objects.create(**data)

    def update(self, solicitacao):
        return Solicitacao.objects.update(solicitacao)

    def delete(self, id):
        return Solicitacao.objects.delete(id)

    def get_all(self):
        return Solicitacao.objects.all()

    def get_by_id(self, id):
        return Solicitacao.objects.get(id=id)

    def filter(self, **kwargs):
        return Solicitacao.objects.filter(**kwargs)
