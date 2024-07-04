from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User, PasswordCompany


class TestUser(APITestCase):
    """
        Тестирование создание пользователя
    """
    def setUp(self):
        self.user = User.objects.create(email='admin@test.com')
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):

        data = {
            "email": "test@example.com",
            "password": 1234
        }
        url = reverse('users:users-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {'id': response.json()['id'],
             "password": response.json()['password'],
             "email": "test@example.com",
             "city": None,
             "company_count": 0,
             "first_name": "", 'date_joined': response.json()['date_joined'],
             "groups": [],
             "image": None,
             "is_active": True,
             "is_staff": False,
             "is_superuser": False,
             "last_login": None,
             "last_name": "",
             "phone": None,
             "user_permissions": []})

        self.assertTrue(User.objects.all().count() == 2)


class PaswordCompanyTestCase(APITestCase):
    """
    Тестирование создания, изменения и получения урока
    """
    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.password = PasswordCompany.objects.create(service_name="www.google.com", password=1234, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_password_create(self):
        url = reverse('users:password_create')
        data = {
            "service_name": "www.yandex.ru",
            "password": 1234,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PasswordCompany.objects.all().count(), 2)

    def test_password_update(self):
        url = reverse('users:password_update', args=(self.password.pk,))
        data = {
            "service_name": "www.google.com",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('service_name', ), "www.google.com", )

    def test_password_retrieve(self):
        url = reverse('users:password_detail', args=(self.password.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('service_name', 'password'), "www.google.com", 1234)

    def test_password_delete(self):
        url = reverse('users:password_delete', args=(self.password.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PasswordCompany.objects.all().count(), 0)

    def test_password_list(self):
        url = reverse('users:password_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': self.password.id,
                               'service_name': response.json()['results'][0]['service_name'],
                               'password': "1234",
                               'owner': self.password.owner.id}]}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
