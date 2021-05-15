from django.views import generic
from ..models import Message


class MessageListAPIView(generic.ListView):
    template_name = 'chat/message.html'
    queryset = Message.objects.all()
