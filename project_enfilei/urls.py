from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

api_urls = [
    # path("base/", include("base.urls")),
    # path("usuario/", include("usuario.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

outras_urls = [
    path("admin/", admin.site.urls),
    path("swagger/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

urlpatterns = [
    path("", include(outras_urls)),
    path("api/", include(api_urls)),
]
