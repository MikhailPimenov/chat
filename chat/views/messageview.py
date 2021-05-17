from django.contrib.auth import mixins
from django.views import generic
from ..models import Message


class MessageListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'chat/message.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Message.objects.filter(dialog=self.request.GET.get('dialog_id', None))
        return queryset


class MessageCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'chat/message_new.html'
    model = Message
    fields = '__all__'
