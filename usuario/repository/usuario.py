from usuario.models import Usuario, Pessoa


class UsuarioRepository:
    def create(
        self,
        email: str,
        password: str,
        pessoa: Pessoa,
    ):
        return Usuario.objects.create_user(  # Do manager
            email=email,
            password=password,
            pessoa=pessoa,
        )

    def update(self, usuario):
        return Usuario.objects.update(usuario)

    def delete(self, id):
        return Usuario.objects.delete(id)

    def get_all(self, active=True):
        return Usuario.objects.filter(is_active=active)

    def get_by_id(self, id, active=True):
        return Usuario.objects.get(id=id, is_active=active)

    def filter(self, **kwargs):
        return Usuario.objects.filter(**kwargs)
