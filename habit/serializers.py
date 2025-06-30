from rest_framework import serializers

from habit.models import Habit
from habit.validators import validate_reward_linked_habit, validate_time_complete, validate_linked_habit_is_enjoy, \
    validate_is_enjoy_habit, validate_periodically


class HabitSerializer(serializers.ModelSerializer):
    '''Сериализатор привычки'''

    def validate(self, data):

        habit = Habit(**data)

        validate_reward_linked_habit(habit)
        validate_time_complete(habit)
        validate_linked_habit_is_enjoy(habit)
        validate_is_enjoy_habit(habit)
        validate_periodically(habit)

        return data

    class Meta:
        model = Habit
        fields = "__all__"
