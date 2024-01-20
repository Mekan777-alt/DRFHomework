from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.api.serializers.registration import RegistrationSerializer
from users.api.serializers.user import UserDetailSerializer


@extend_schema(
    summary='Регистрация в системе',
    tags=['Auth'],
    request=RegistrationSerializer,
    responses={
        201: RegistrationSerializer,
        400: ...
    }
)
@api_view(['POST'])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    user_serializer = UserDetailSerializer(instance=user)

    return Response(data=user_serializer.data, status=status.HTTP_201_CREATED)
