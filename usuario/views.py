from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_spectacular.utils import extend_schema


from usuario.serializers import MyTokenObtainPairSerializer
from usuario.models import Usuario
from usuario.serializers import UsuarioCreateSerializer, UsuarioListSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@extend_schema(tags=["usuario"])
class UsuarioView(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Usuario.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def check_permissions(self, request):
        # if self.action == "patch":
        #     self.permission_classes = [IsAuthenticated]
        return super().check_permissions(request)

    def get_queryset(self):
        return super().get_queryset().filter()

    def get_serializer_class(self):
        if self.action == "create":
            return UsuarioCreateSerializer
        return UsuarioListSerializer
