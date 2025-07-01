from celery import shared_task

from habit.models import Habit

from .services import send_message


@shared_task
def sending_message_telegram(chat_id, habit_id):
    """Сообщение в телеграм чат с деталями привычки"""

    habit = Habit.objects.get(id=habit_id)
    message = (
        f"Вы создали новую привычку:\n"
        f"Место выполнения: {habit.location}\n"
        f"Действие, которое нужно выполнять: {habit.action}\n"
        f"Время, когда начать совершенствоваться: {habit.time}"
        f"Она для Вас приятная? (True-да/False-нет: {habit.is_enjoy}"
        f"Действие нужно сделать за: {habit.time_complete}\n"
        f"Помните, мы сами создаем себя и это главная мотивация"
    )
    send_message(message, chat_id)
