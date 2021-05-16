from django.contrib.auth import mixins
from django.views import generic
from ..models import Dialog


class DialogListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'chat/dialog.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Dialog.objects.filter(users=self.request.user.id)
        return queryset

