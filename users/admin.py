from django.contrib import admin

from users.models import User, PasswordCompany


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка для модели User
    """
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')


@admin.register(PasswordCompany)
class PasswordCompanyAdmin(admin.ModelAdmin):
    """
    Админка для модели PasswordCompany
    """
    list_display = ('id', 'service_name', 'password', 'owner')
