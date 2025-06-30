from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Класс тестирования модели пользователя и его функционал"""

    def setUp(self):

        self.user = User.objects.create(
            email="test@test.com",
            tg_chat_id=123123123,
        )

        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        """Тестирование просмотра списка пользователей"""

        url = reverse("users:user-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {"id": self.user.pk, "email": "test@test.com", "tg_chat_id": "123123123"},
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_user_retrieve(self):
        """Тестирование получения одного пользователя"""

        url = reverse("users:user-detail", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), self.user.email)

    def test_user_create(self):
        """Тестирование создания пользователя"""

        url = reverse("users:user-list")

        data = {"email": "testuser@testuser.ru", "password": "4123qwe4123rty", "tg_chat_id": "14253"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_user_update(self):
        """Тестирование обновления пользователя"""

        url = reverse("users:user-detail", args=(self.user.pk,))

        data = {"tg_chat_id": 111222333, "password": "qwe123qwe"}
        response = self.client.patch(url, data)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("tg_chat_id"), "111222333")

    def test_lesson_delete(self):
        """Тестирование удаления пользователя"""

        url = reverse("users:user-detail", args=(self.user.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
