from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.enums import Groups
from users.models import User


class RegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)
    confirm_password = serializers.CharField(max_length=255, write_only=True)
    is_backer = serializers.BooleanField(write_only=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с такой почтой уже есть в системе')

        return email

    def validate_password(self, password):
        validate_password(password)

        return password

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError('Пароли не совпадают')

        return super().validate(attrs)

    def create(self, validated_data):
        name = Groups.BACKER.name if validated_data.get('is_backer') else Groups.CREATOR.name

        group = Group.objects.get(name=name)

        user = User.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email')
        )
        user.set_password(validated_data.get('password'))
        user.save()

        user.groups.add(group)

        return user
