from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["grupos"] = list(user.groups.values_list("name", flat=True))
        token["permissoes"] = list(
            user.user_permissions.values_list("codename", flat=True)
        )
        token["permissoes_grupo"] = list(
            user.get_group_permissions()
        )
        return token
