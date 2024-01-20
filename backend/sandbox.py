import os
from django.apps import apps
from rest_framework_simplejwt.tokens import AccessToken
import django

# Установка ссылки на конфиг приложения
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

User = apps.get_model("users", "User")

# Генерируем секрет для юзера, который хочет изменить пароль
access = AccessToken.for_user(User.objects.get(pk=1))

# Валидируем и получаем айдишник юзера.
# При вызове AccessToken() происходит валидация токена, если он невалидный, выбрасывается исключение.
token_data = AccessToken(str(access))
user_id = token_data['user_id']
