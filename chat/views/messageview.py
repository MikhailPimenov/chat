from django.contrib.auth import mixins
from django.views import generic
from ..models import Message, Dialog
from ..forms import MessageModelForm


class MessageListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'chat/message.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Message.objects.filter(dialog=self.request.GET.get('dialog_id', None))
        return queryset


class MessageCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'chat/message_new.html'
    model = Message
    form_class = MessageModelForm

    def post(self, request, *args, **kwargs):
        print('request:', request.POST.get('content'))
        request.POST.__setitem__('dialog_id', 1)
        # content = request.POST.get('content')
        # dialog = Dialog.objects.get(id=1)
        # self.object = Message.objects.create(content=content, dialog=dialog)
        return super().post(request, *args, **kwargs)
