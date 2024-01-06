from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.api.serializers.project_update import ProjectUpdateSerializer
from projects.models import ProjectUpdate, Project


class ProjectUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectUpdateSerializer
    queryset = ProjectUpdate.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        project = get_object_or_404(Project.objects.filter(pk=kwargs.get('pk'), user=request.user))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(project=project)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
