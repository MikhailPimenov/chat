from django.contrib.auth.models import User
from django.db import models


class Dialog(models.Model):
    users = models.ManyToManyField(User)
    start_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "dialog"
        verbose_name_plural = "dialogs"

    def __str__(self):
        return f"dialog #{self.id} started at {self.start_time}"
