from django.contrib.auth import mixins
from django.views import generic
from ..models import Message
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


class MessageCreateFormView(mixins.LoginRequiredMixin, generic.FormView):
    #  TODO: is it correct to use FormView here?
    template_name = 'chat/message_new.html'
    form_class = MessageModelForm

    def get_context_data(self, **kwargs):
        context = {
            'dialog_id': self.request.GET.get('dialog_id', None),
            'form': self.form_class,  # TODO: is it better to use self.get_form_class() here?
        }
        return context


class MessageCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Message
    fields = '__all__'
