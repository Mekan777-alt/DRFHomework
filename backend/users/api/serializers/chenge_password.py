from rest_framework import serializers
from django.db import models
from users.models import User


class ChangePasswordSerializers(serializers.Serializer):
    email = models.EmailField()

    def validate_email(self, email):
        if User.objects.filter(email).exists():
            return email
        raise serializers.ValidationError("Данного пользователя не существует")
