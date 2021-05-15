from django.db import models
from django.contrib.auth.models import User


class Dialog(models.Model):
    users = models.ManyToManyField(User)
    started_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'dialog'
        verbose_name_plural = 'dialogs'

    def __str__(self):
        return f'dialog #{self.id} started at {self.started_time}'
