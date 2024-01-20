from rest_framework import serializers
from projects.models import Pledge


class PledgeSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=19, decimal_places=2, max_value=1)

    def validate_amount(self, amount):
        wallet = self.context['request'].user.get_wallet()

        if wallet.funds < amount:
            raise serializers.ValidationError('Не достаточно денег в кошельке')

        return amount

    def create(self, validated_data):
        amount = validated_data.get('amount')

        wallet = self.context['request'].user.get_wallet()
        wallet.funds = wallet.funds - amount
        wallet.save()

        project = validated_data.get('project')
        project.current_amount += amount
        project.save()

        return Pledge.objects.create(**validated_data)
