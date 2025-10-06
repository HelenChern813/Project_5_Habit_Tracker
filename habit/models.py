from django.db import models

from config.settings import AUTH_USER_MODEL


class Habit(models.Model):
    """Модель привычки"""

    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пользователь"
    )
    location = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_enjoy = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    linked_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанная привычка"
    )
    periodically = models.PositiveIntegerField(default=1, verbose_name="Периодичность в днях")
    reward = models.CharField(max_length=255, blank=True, null=True, verbose_name="Вознаграждение")
    time_complete = models.PositiveIntegerField(default=60, verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return f"Пользователь {self.user} будет выполнять привычку в {self.location}, время {self.time}, действие: {self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["pk", "user"]
