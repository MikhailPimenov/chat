from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.views import generic
from ..models import Message, Blacklist, Dialog
from ..forms import MessageModelForm


class MessageListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'chat/message.html'

    def get_owner_and_interlocutor(self):
        owner = self.request.user
        dialog = Dialog.objects.get(id=self.request.GET.get('dialog_id', None))
        interlocutor1, interlocutor2 = dialog.users.all()
        interlocutor = interlocutor1 if owner != interlocutor1 else interlocutor2
        return owner, interlocutor

    def is_user_blocked(self, owner, interlocutor):
        blacklist = Blacklist.objects.get(owner=owner)
        if interlocutor in blacklist.blocked_users.all():
            return True
        return False

    def get_queryset(self, *args, **kwargs):
        queryset = Message.objects.filter(dialog=self.request.GET.get('dialog_id', None))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        owner, interlocutor = self.get_owner_and_interlocutor()
        context = {
            'object_list': self.get_queryset(**kwargs),  # TODO: is it correct?
            'dialog_id': self.request.GET.get('dialog_id', None),
            'is_blocked': self.is_user_blocked(owner, interlocutor),
            'is_blocked_by_user': self.is_user_blocked(interlocutor, owner),
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
