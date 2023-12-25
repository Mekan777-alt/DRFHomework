from django.db import models


class UserWallet(models.Model):
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        primary_key=True
    )

    funds = models.DecimalField('Доступные средства', decimal_places=2, max_digits=19, default=0)
