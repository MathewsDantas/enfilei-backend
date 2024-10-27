import requests
from django.core.management.base import BaseCommand
from django.db import transaction

from base.models import BaseEstado, BaseMunicipio, BaseBairro

# #Municipio
# {
#     "id": 1100015,
#     "nome": "Alta Floresta D'Oeste",
#     "microrregiao": {
#       "id": 11006,
#       "nome": "Cacoal",
#       "mesorregiao": {
#         "id": 1102,
#         "nome": "Leste Rondoniense",
#         "UF": {
#           "id": 11,
#           "sigla": "RO",
#           "nome": "Rondônia",
#           "regiao": {
#             "id": 1,
#             "sigla": "N",
#             "nome": "Norte"
#           }
#         }
#       }
#     },


class Command(BaseCommand):
    help = "Seed IBGE"

    def fetch_data(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @transaction.atomic
    def seed_estados(self):
        estados = self.fetch_data(
            "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
        )
        for estado in estados:
            BaseEstado.objects.get_or_create(
                id=estado["id"],
                defaults={
                    "descricao": estado["nome"],
                    "sigla": estado["sigla"],
                },
            )

    @transaction.atomic
    def seed_municipios(self):
        municipios = self.fetch_data(
            "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
        )
        for municipio in municipios:
            BaseMunicipio.objects.get_or_create(
                id=municipio["id"],
                defaults={
                    "descricao": municipio["nome"],
                    "estado": BaseEstado.objects.get(
                        id=municipio["microrregiao"]["mesorregiao"]["UF"]["id"]
                    ),  # noqa
                },
            )

    @transaction.atomic
    def seed_bairros(self):
        bairros = self.fetch_data(
            "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
        )
        for bairro in bairros:
            estado = BaseEstado.objects.get(
                id=bairro["municipio"]["microrregiao"]["mesorregiao"]["UF"]["id"]
            )
            municipio = BaseMunicipio.objects.get(id=bairro["municipio"]["id"])
            BaseBairro.objects.get_or_create(
                id=bairro["id"],
                defaults={
                    "descricao": bairro["nome"],
                    "municipio": municipio,
                    "estado": estado,
                },
            )

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding Estados...")
        self.seed_estados()
        self.stdout.write("Seeding Municipios...")
        self.seed_municipios()
        self.stdout.write("Seeding Bairros...")
        self.seed_bairros()
        self.stdout.write(self.style.SUCCESS("IBGE data seeded successfully"))
