from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import User, PasswordCompany


class PasswordCompanySerializer(ModelSerializer):
    """
    Сериализатор для модели User
    """
    # company_count = SerializerMethodField()

    class Meta:
        model = PasswordCompany
        fields = '__all__'


class UserSerializer(ModelSerializer):
    """
    Сериализатор для модели User
    """
    company_count = SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_company_count(self, obj):
        if obj.passwordcompany_set.all().count():
            return obj.passwordcompany_set.all().count()
        return 0
