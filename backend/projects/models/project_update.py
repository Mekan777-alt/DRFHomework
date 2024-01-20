from django.db import models


class ProjectUpdate(models.Model):
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='updates'
    )

    name = models.CharField('Название', max_length=255)

    description = models.TextField('Описание')

    created = models.DateTimeField('Дата создания', auto_now_add=True)
