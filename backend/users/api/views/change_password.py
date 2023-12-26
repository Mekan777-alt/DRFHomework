from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from users.tasks import send_password_reset_email


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def reset_password(request):
    email = request.data.get('email')

    if email:
        user = get_user_model().objects.filter(email=email).first()

        if user:
            token = AccessToken.for_user(user)

            reset_link = f"api/auth/change-password?secret={str(token)}"

            send_password_reset_email.delay(email, reset_link)

            return Response({'detail': f'Ссылка для сброса пароля успешно отправлена. {reset_link}'}, status=status.HTTP_200_OK)

    return Response({'detail': 'Неверный адрес электронной почты.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def change_password(request):
    token = request.GET.get("secret", None)
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if token and password == confirm_password:
        try:
            decoded_token = AccessToken(token)
            user_id = decoded_token['user_id']

            user = get_object_or_404(get_user_model(), pk=user_id)

            user.password = make_password(password)
            user.save()

            refresh_token = RefreshToken.for_user(user)
            refresh_token.blacklist_after = None  # добавление в черный список

            return Response({'detail': 'Пароль успешно изменен.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": str(e)})

    return Response({'detail': 'Недействительный токен или несоответствие пароля.'}, status=status.HTTP_400_BAD_REQUEST)
