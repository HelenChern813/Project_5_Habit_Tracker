from rest_framework.exceptions import ValidationError


def validate_reward_linked_habit(habit):
    """Не указаны одновременно вознаграждение и связанная привычка."""

    if habit.reward and habit.linked_habit:
        raise ValidationError("Нельзя указывать одновременно вознаграждение и связанную привычку.")


def validate_time_complete(habit):
    """Время выполнения не превышает 120 секунд."""

    if habit.time_complete > 120:
        raise ValidationError("Время выполнения привычки не должно превышать 120 секунд.")


def validate_linked_habit_is_enjoy(habit):
    """Связанная привычка является приятной."""

    if habit.linked_habit and not habit.is_enjoy:
        raise ValidationError("Связанная привычка должна быть приятной. Она должна радовать вас")


def validate_is_enjoy_habit(habit):
    """У приятной привычки нет вознаграждения или связанной привычки."""

    if habit.is_enjoy and (habit.reward or habit.linked_habit):
        raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки. Выполняя ее вы уже становитесь счастливее")


def validate_periodically(habit):
    """Выполнение не реже, чем 1 раз в 7 дней."""

    if habit.periodically > 7:
        raise ValidationError("Привычку нужно выполнять не реже, чем 1 раз в 7 дней.")
    if habit.periodically == 0:
        raise ValidationError("Поставь выполнение хотя бы 1 раз в 7 дней, иначе привычка может не сформироваться.")
