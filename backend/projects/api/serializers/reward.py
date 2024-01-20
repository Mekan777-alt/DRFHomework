from rest_framework import serializers
from projects.models import Reward


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['project', 'name', 'description', 'minimum_amount']
