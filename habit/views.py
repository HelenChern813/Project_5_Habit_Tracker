from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwner

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer
from habit.tasks import sending_message_telegram


class HabitCreateAPIView(CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):

        habit = serializer.save(user=self.request.user)

        habit_details = {
            "location": habit.location,
            "action": habit.action,
            "time": habit.time.strftime("%H:%M:%S"),
        }
        sending_message_telegram.delay(
            chat_id=self.request.user.tg_chat_id,
            habit_details=habit_details
        )


class HabitUpdateAPIView(UpdateAPIView):
    """Изменение привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """Удаление привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(RetrieveAPIView):
    """Получение одной привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListAPIView(ListAPIView):
    """Получение списка привычек"""

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Фильтрация по пользователю"""

        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitPublicListAPIView(ListAPIView):
    """Получение списка публичных привычек"""

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Фильтрация публичных привычек"""

        return Habit.objects.filter(is_public=True)
