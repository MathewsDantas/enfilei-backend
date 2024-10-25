from django.urls import path, include
from rest_framework.routers import DefaultRouter


from solicitacao.views import SolicitacaoViewSet


router = DefaultRouter()

router.register("", SolicitacaoViewSet, basename="solicitacao")

solicitacoes_urls = [
    path("", include(router.urls)),
]
