from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserViewSet, PasswordCompanyCreateAPIView, PasswordCompanyListAPIView, \
    PasswordCompanyRetrieveAPIView, PasswordCompanyUpdateAPIView, PasswordCompanyDestroyAPIView

app_name = UsersConfig.name
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # токен для пользователя
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # CRUD компаний
    path('password/', PasswordCompanyCreateAPIView.as_view(), name='password_create'),
    path('', PasswordCompanyListAPIView.as_view(), name='password_list'),
    path('<int:pk>/', PasswordCompanyRetrieveAPIView.as_view(), name='password_detail'),
    path('update/<int:pk>/', PasswordCompanyUpdateAPIView.as_view(), name='password_update'),
    path('delete/<int:pk>/', PasswordCompanyDestroyAPIView.as_view(), name='password_delete'),
] + router.urls
