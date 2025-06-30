from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habit.models import Habit
from users.models import User


class HabitTests(APITestCase):
    """Класс теста модели привычки и её функционала"""

    def setUp(self):

        self.user = User.objects.create(
            email='test@test.com',
            password='qwe123qwe'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            location="Где угодно",
            time="10:00:00",
            action="Выпить стакан воды",
            is_enjoy=False,
            periodically=1,
            reward=None,
            execution_time=30,
            is_public=False
        )

    def test_habit_create(self):
        """Тестирование создания привычки"""

        url = reverse('habit:habit_create')
        data = {
            "location": "У себя дома",
            "time": "19:00:00",
            "action": "Приготовить ужин",
            "is_enjoy": True,
            "periodically": 2,
            "reward": 'Вкусный ужин',
            "time_complete": 90,
            "is_public": False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_update(self):
        """Тестирование обновления привычки"""

        url = reverse('habit:habit_update', args=[self.habit.id])
        data = {
            "location": "Где угодно, если тебе удобно"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, "Бегать на улице")

    def test_habit_delete(self):
        """Тестирование удаления привычки"""

        url = reverse('habit:habit_delete', args=[self.habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_habit_retrieve(self):
        """Тестирование получения одной привычки"""

        url = reverse('habit:habit_retrieve', args=[self.habit.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['location'], self.habit.location)

    def test_habit_list(self):
        """Тестирование получения списка привычек"""

        url = reverse('habit:habit_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
