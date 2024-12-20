from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from drf_spectacular.utils import extend_schema, extend_schema_view

from usuario.views import MyTokenObtainPairView, UsuarioView, PessoaView

router = DefaultRouter()

router.register("usuario", UsuarioView, basename="usuario")
router.register("pessoa", PessoaView, basename="pessoa")

auth_urls = [
    path(
        "login/",
        extend_schema_view(
            post=extend_schema(
                tags=["auth"],
                summary="Obtain Pair JWT token",
            )
        )(MyTokenObtainPairView.as_view()),
        name="token_obtain_pair",
    ),
    path(
        "refresh/",
        extend_schema_view(
            post=extend_schema(
                tags=["auth"],
                summary="Refresh JWT token",
            )
        )(TokenRefreshView.as_view()),
        name="token_refresh",
    ),
]

usuario_urls = [
    path("auth/", include(auth_urls)),
    path("", include(router.urls)),
]
