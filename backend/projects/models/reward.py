from django.db import models
from projects.models import Project


class Reward(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    minimum_amount = models.DecimalField(decimal_places=2, max_digits=19)

    def __str__(self):
        return f"{self.project} - {self.name}"
