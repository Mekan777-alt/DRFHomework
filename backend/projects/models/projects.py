from django.db import models
from users.models import User


class Project(models.Model):
    class Status(models.TextChoices):
        FUNDED = 'Профинансирован', 'funded'
        IN_PROGRESS = 'В процесе финансирования', 'in_progress'
        CANCELLED = 'Отменен', 'cancelled'
        ON_MODERATION = 'На модерации', 'on_moderation'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField('Название', max_length=255)

    description = models.TextField('Описание')

    total_amount = models.DecimalField('Сумма для сбора', decimal_places=2, max_digits=19)

    current_amount = models.DecimalField('Текущая собранная сумма', decimal_places=2, max_digits=19)

    deadline = models.DateTimeField('Дедлайн')

    status = models.CharField('Статус', choices=Status.choices)

    is_approved = models.BooleanField('Прошел модерацию', null=True)

    def __str__(self):
        return self.name
