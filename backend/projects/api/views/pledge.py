from rest_framework import viewsets, status, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projects.api.serializers.pledge import PledgeSerializer
from projects.models import Project, Pledge


class PledgeViewSet(viewsets.ModelViewSet):
    serializer_class = PledgeSerializer
    queryset = Pledge.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        project = get_object_or_404(Project.objects.filter(pk=kwargs.get('pk')))
        pledge = Pledge.objects.filter(project=project, user=request.user).first()

        if pledge is not None:
            return Response(
                {'error': 'Пользователь уже финансировал этот проект'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(project=project, user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
