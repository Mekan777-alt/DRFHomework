from django.db import models
from django.contrib.auth.models import AbstractUser
from users.orm_managers import UserManager


class User(AbstractUser):
    object = UserManager()

    email = models.EmailField('Электронная почта', unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)

    username = None

    def get_wallet(self):
        from users.models import UserWallet

        wallet, _ = UserWallet.objects.get_or_create(user=self)

        return wallet

