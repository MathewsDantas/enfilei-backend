from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


from usuario.permissions.permission_admin import get_permissoes_admin

from usuario.permissions.permission_gerente import get_permissoes_gerente
from usuario.permissions.permission_caixa import get_permissoes_caixa
from usuario.permissions.permission_cozinheiro import get_permissoes_cozinheiro
from usuario.permissions.permission_garcom import get_permissoes_garcom
from usuario.permissions.permission_terceirizado import get_permissoes_terceirizado
from usuario.permissions.permission_cliente import get_permissoes_cliente


class Command(BaseCommand):
    help = "Cria grupos e permissoes"

    def handle(self, *args, **kwargs):
        self.stdout.write("Criando grupos e permissoes...")
        grupos_e_permissoes = {
            **get_permissoes_admin(),
            **get_permissoes_gerente(),
            **get_permissoes_caixa(),
            **get_permissoes_cozinheiro(),
            **get_permissoes_garcom(),
            **get_permissoes_terceirizado(),
            **get_permissoes_cliente(),
        }

        # [('admin', [{'codename': 'perm1', 'contentcontent_type', 'queijo'}, ...], ...)]
        for grupo_dict, permissoes_dict in grupos_e_permissoes.items():
            grupo, criado = Group.objects.get_or_create(name=grupo_dict)

            if not criado:
                permissoes_atual_grupo = set(grupo.permissions.all())
                permissoes_novas = set()
                for permissao in permissoes_dict:
                    perm, criado = Permission.objects.get_or_create(
                        codename=permissao["codename"],
                        content_type=permissao["content_type"],
                        name=permissao["name"],
                    )
                    permissoes_novas.add(perm)
                # Remover permissoes que nao devem mais estar no grupo
                permissoes_a_remover = permissoes_atual_grupo - permissoes_novas
                if permissoes_a_remover:
                    grupo.permissions.remove(
                        *permissoes_a_remover
                    )  # esse * é para desempacotar o set exemplo: set(1,2,3) -> 1,2,3

            # Adicionar permissoes ao grupo
            for permissao in permissoes_dict:
                try:
                    perm, criado = Permission.objects.get_or_create(
                        codename=permissao["codename"],
                        content_type=permissao["content_type"],
                        name=permissao["name"],
                    )

                    grupo.permissions.add(perm)
                    print(f"Permissao {permissao} adicionada ao grupo {grupo}")
                except Permission.DoesNotExist:
                    print(f"Permissao {permissao} nao encontrada")

        self.stdout.write(
            "Grupos e permissoes criados com sucesso!", style_func=self.style.SUCCESS
        )
