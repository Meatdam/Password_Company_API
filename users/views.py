from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import make_password

from users.models import User, PasswordCompany
from users.paginators import Paginator
from users.permissions import IsModerator, IsOwner
from users.serializers import UserSerializer, PasswordCompanySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Course
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """
        Хеширование пароля
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PasswordCompanyCreateAPIView(generics.CreateAPIView):
    serializer_class = PasswordCompanySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Перед сохранением компании и пароля добавляем владельца
        """
        company = serializer.save()
        company.owner = self.request.user
        company.password = make_password(company.password)
        company.save()


class PasswordCompanyListAPIView(generics.ListAPIView):
    """
    API для получения списка уроков
    """
    serializer_class = PasswordCompanySerializer
    queryset = PasswordCompany.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Paginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'service_name', 'password']

    def get_queryset(self):
        """
        Получаем список компаний в зависимости от прав пользователя
        """
        if IsModerator().has_permission(self.request, self):
            return PasswordCompany.objects.all()
        else:
            return PasswordCompany.objects.filter(owner=self.request.user)


class PasswordCompanyRetrieveAPIView(generics.RetrieveAPIView):
    """
    API для получения компании и пароля
    """
    serializer_class = PasswordCompanySerializer
    queryset = PasswordCompany.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class PasswordCompanyUpdateAPIView(generics.UpdateAPIView):
    """
    API для изменения пароля и компании
    """
    serializer_class = PasswordCompanySerializer
    queryset = PasswordCompany.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)

    def perform_update(self, serializer):
        """
        Перед сохранением компании и хешируем пароль
        """
        company = serializer.save()
        company.password = make_password(company.password)
        company.save()


class PasswordCompanyDestroyAPIView(generics.DestroyAPIView):
    """
    API для удаления пароля и компании
    """
    queryset = PasswordCompany.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)
