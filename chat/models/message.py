from django.db import models
from django.urls import reverse
from django.http import QueryDict


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

    def get_absolute_url(self):
        query_dictionary = QueryDict('', mutable=True)
        query_dictionary.update(
            {
                'dialog_id': self.dialog.id,
            }
        )
        url = '{base_url}?{querystring}'.format(
            base_url=reverse(viewname="messages_name"),
            querystring=query_dictionary.urlencode()
        )

        return url
