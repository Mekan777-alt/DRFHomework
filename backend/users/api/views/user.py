from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.api.serializers.user import UserDetailSerializer, UserUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = request.user
        update_serializer = self.get_serializer(user, data=request.data, partial=partial)
        update_serializer.is_valid(raise_exception=True)
        self.perform_update(update_serializer)

        detail_serializer = UserDetailSerializer(instance=user)

        if getattr(user, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            user._prefetched_objects_cache = {}

        return Response(detail_serializer.data)

    def retrieve(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(instance=request.user)

        return Response(serializer.data)
