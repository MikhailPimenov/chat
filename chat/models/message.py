from django.db import models


class Message(models.Model):
    content = models.TextField(max_length=50)

    dialog = models.ForeignKey(
        'Dialog',
        related_name='messages',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    send_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return f'message #{self.id} from dialog {self.dialog} sent at {self.send_time}'
