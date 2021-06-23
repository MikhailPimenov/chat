from django.contrib.auth.models import User
from django.db import models


class Blacklist(models.Model):
    owner = models.ForeignKey(
        User,
        related_name="own_blacklist",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    blocked_users = models.ManyToManyField(User)

    class Meta:
        verbose_name = "blacklist"
        verbose_name_plural = "blacklists"

    def __str__(self):
        return f'{self.owner.username}"s blacklist'
