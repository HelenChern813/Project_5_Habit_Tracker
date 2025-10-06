from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "tg_chat_id",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        user = User(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):

        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
