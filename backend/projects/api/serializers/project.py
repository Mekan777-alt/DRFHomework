from rest_framework import serializers

from projects.models import Project


class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    total_amount = serializers.DecimalField(min_value=1, max_digits=19, decimal_places=2)
    deadline = serializers.DateTimeField()


class ProjectCreateUpdateSerializer(ProjectSerializer):
    def create(self, validated_data):
        project = Project.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            total_amount=validated_data.get('total_amount'),
            deadline=validated_data.get("deadline"),
            user=self.context['request'].user,
            status=Project.Status.ON_MODERATION.value,
            current_amount=0
        )

        return project

    def update(self, instance, validated_data):
        instance.total_amount = validated_data.get('total_amount')
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.deadline = validated_data.get('deadline')
        instance.save()

        return instance


class ProjectListDetailSerializer(ProjectSerializer):
    id = serializers.IntegerField()
    current_amount = serializers.DecimalField(max_digits=19, decimal_places=2)
    status = serializers.CharField()
