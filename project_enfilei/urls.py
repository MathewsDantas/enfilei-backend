from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


from usuario.urls import usuario_urls
from solicitacao.urls import solicitacoes_urls

api_urls = [
    # path("base/", include("base.urls")),
    path("usuario/", include(usuario_urls)),
    path("solicitacao/", include(solicitacoes_urls)),
]

outras_urls = [
    path("admin/", admin.site.urls),
    path("swagger/yaml", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

urlpatterns = [
    path("api/", include(api_urls)),
    path("", include(outras_urls)),
]
