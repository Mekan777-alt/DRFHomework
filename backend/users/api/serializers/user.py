from rest_framework import serializers

from users.api.serializers.group import GroupSerializer


class UserDetailSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    group = serializers.SerializerMethodField()

    def get_group(self, user):
        group = user.groups.first()

        return GroupSerializer(group).data
