from django.contrib.auth import mixins
from django.views import generic
from ..models import Message


class MessageListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'chat/message.html'

    def get_queryset(self, *args, **kwargs):
        # print(self.request)
        # print('fucking dialog_id', self.kwargs['dialog_id'], self.)
        # print('fucking id', self.request.GET.get('dialog_id', None))
        queryset = Message.objects.filter(dialog=self.request.GET.get('dialog_id', None))
        return queryset

    # def get(self, request):
    #     print('fucking request', request)
    #     print('query parameters', request.query_params)