from rest_framework import serializers

from projects.models import ProjectUpdate


class ProjectUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=5000)
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ProjectUpdate.objects.create(
            name=validated_data.get("name"),
            description=validated_data.get("description"),
            project=validated_data.get('project')
        )
