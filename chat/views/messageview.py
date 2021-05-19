from django.contrib.auth import mixins
from django.shortcuts import render
from django.views import generic
from ..models import Message, Dialog
from ..forms import MessageModelForm


class MessageListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'chat/message.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Message.objects.filter(dialog=self.request.GET.get('dialog_id', None))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'object_list': self.get_queryset(**kwargs),  # TODO: is it correct?
            'dialog_id': self.request.GET.get('dialog_id', None),
        }
        return context


def message_create_render_view(request):
    print('message_create_render_view!!!')
    print('dialog_id:', request.GET.get('dialog_id', None))
    context = {
        'dialog_id': request.GET.get('dialog_id', None),
        'form': MessageModelForm,
    }
    return render(request, 'chat/message_new.html', context)


class MessageCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    # pass
    # template_name = 'chat/message_new.html'
    model = Message
    fields = '__all__'
    # form_class = MessageModelForm
    #
    # def render_to_response(self, context, **response_kwargs):
    #     print('render_to_response()')
    #     print('dialog_id:', self.request.GET.get('dialog_id', None))
    #     context = {
    #         'dialog_id': self.request.GET.get('dialog_id', None),
    #         'form': MessageModelForm,
    #     }
    #     return self.response_class(
    #         request=self.request,
    #         template='chat/message_new.html',
    #         context=context,
    #     )
    #
    # def post(self, request, *args, **kwargs):
    #     print('request.POST.content:', request.POST.get('content'))
    #     print('request.POST.dialog_id:', request.POST.get('dialog'))
    #     print('request.POST:', request.POST)
    #     dialog = Dialog.objects.get(id=request.POST.get('dialog'))
    #     # request.POST.__setitem__('dialog_id', 1)
    #     content = request.POST.get('content')
    #     # dialog = Dialog.objects.get(id=1)
    #     self.object = Message.objects.create(content=content, dialog=dialog)
    #     return super().post(request, *args, **kwargs)
