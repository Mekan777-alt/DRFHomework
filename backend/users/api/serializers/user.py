from rest_framework import serializers

from users.api.serializers.group import GroupSerializer
from users.models import UserWallet


class UserDetailSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(required=False)
    group = serializers.SerializerMethodField()
    funds = serializers.SerializerMethodField()

    def get_group(self, user):
        group = user.groups.first()

        return GroupSerializer(group).data

    def get_funds(self, user):
        wallet = user.get_wallet()

        return wallet.funds


class UserUpdateSerializer(UserDetailSerializer):
    # TODO: implement email validation

    funds = serializers.DecimalField(max_digits=19, decimal_places=2, min_value=1)

    def update(self, user, validated_data):
        user.email = validated_data.get("email", user.email)
        user.first_name = validated_data.get("first_name", user.first_name)
        user.last_name = validated_data.get("last_name", user.last_name)
        user.save()

        funds = validated_data.get('funds')

        if funds is not None:
            wallet = user.get_wallet()
            wallet.funds = wallet.funds + funds
            wallet.save()

        return user
