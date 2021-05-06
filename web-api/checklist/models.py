from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class TaskModel(models.Model):
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
