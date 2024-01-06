from projects.tasks import send_mail
from django.db import models


class Project(models.Model):
    class Status(models.TextChoices):
        FUNDED = 'Профинансирован'
        IN_PROGRESS = 'В процесе финансирования'
        CANCELLED = 'Отменен'
        ON_MODERATION = 'На модерации'

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )

    name = models.CharField('Название', max_length=255)

    description = models.TextField('Описание')

    total_amount = models.DecimalField('Сумма для сбора', decimal_places=2, max_digits=19)

    current_amount = models.DecimalField(
        'Текущая собранная сумма', decimal_places=2, max_digits=19, default=0
    )

    deadline = models.DateTimeField('Дедлайн')

    status = models.CharField('Статус', choices=Status.choices, default=Status.ON_MODERATION.value)

    is_approved = models.BooleanField('Прошел модерацию', null=True)

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.current_amount >= self.total_amount:
            send_mail.delay(self.id)

        return super().save(force_insert, force_update, using, update_fields)
