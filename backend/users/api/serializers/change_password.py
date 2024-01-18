from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    secret = serializers.CharField()
    password = serializers.CharField(write_only=True)
    change_password = serializers.CharField(write_only=True)

    def validate(self, data):
        secret = data.get('secret')
        password = data.get('password')
        change_password = data.get('change_password')

        if not secret:
            raise serializers.ValidationError('Отсутствует секретный токен.')

        if password != change_password:
            raise serializers.ValidationError('Пароли не совпадают.')

        return data


