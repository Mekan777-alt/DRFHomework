from django.db import models


class Pledge(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='pledges'
    )

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )

    amount = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        unique_together = (('user', 'project'),)
