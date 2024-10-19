from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from usuario.serializers import MyTokenObtainPairSerializer
from usuario.models import Usuario
from usuario.serializers import UsuarioCreateSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def check_permissions(self, request):
        # if self.action == "patch":
        #     self.permission_classes = [IsAuthenticated]
        return super().check_permissions(request)

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def get_serializer_class(self):
        if self.action == "create":
            return UsuarioCreateSerializer
        return UsuarioCreateSerializer
