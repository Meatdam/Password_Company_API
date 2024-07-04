from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=20, verbose_name='город', **NULLABLE)
    image = models.ImageField(upload_to='user', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class PasswordCompany(models.Model):
    service_name = models.CharField(max_length=200, verbose_name='название компании')
    password = models.CharField(max_length=200, verbose_name='пароль')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.service_name} - {self.owner}'

    class Meta:
        verbose_name = 'пароль компании'
        verbose_name_plural = 'пароли компаний'
