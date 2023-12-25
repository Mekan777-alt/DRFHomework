from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from projects.api.serializers.reward import RewardSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from projects.models import Reward


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class RewardAPIView(APIView):

    @extend_schema(
        summary="Получение списка моделей",
        request=RewardSerializer,
        responses={
            200: RewardSerializer(many=True),
            400: ...
        }
    )
    def get(self, request):
        reward = Reward.objects.all()
        serializer = RewardSerializer(data=reward, many=True)

        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Создайте новую модель",
        request=RewardSerializer,
        responses={
            200: RewardSerializer(),
            400: ...
        }
    )
    def post(self, request):
        serializer = RewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Удаление модели",
        responses={
            204: "Обьект успешно удален",
            400: ...
        }
    )
    def delete(self, request, pk):
        try:
            reward = Reward.objects.get(pk=pk)
        except Reward.DoesNotExist:
            return Response({"message": "Обьект не найден"}, status=status.HTTP_404_NOT_FOUND)

        reward.delete()
        return Response({"message": "Обьект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        summary="Изменение модели",
        request=RewardSerializer,
        responses={
            200: RewardSerializer(),
            400: ...
        }
    )
    def put(self, request, pk):
        try:
            reward = Reward.objects.get(pk=pk)
        except Reward.DoesNotExist:
            return Response({"message": "Обьект не найден"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RewardSerializer(reward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
