from django.db import models
from django.contrib.auth.models import User


class UserDialog(models.Model):
    users = models.ManyToManyField(User)
    dialog = models.ForeignKey(
        'Dialog',
        related_name='user_dialog',
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )

    # class Meta:
    #     unique_together = ('users', 'dialog') #  TODO: find the way to make dialog unique with certain set of users
