from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed all"

    def handle(self, *args, **options):
        call_command("criar_grupos_e_permissoes")
        call_command("seed_ibge")
