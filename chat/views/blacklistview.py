from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from ..models import Blacklist


class BlacklistDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = "chat/blacklist.html"

    def get_object(self, queryset=None):
        return Blacklist.objects.get(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = {
            "object_list": self.get_object().blocked_users.all(),
        }
        return context


def update_blacklist(request):
    blacklist = Blacklist.objects.get(owner=request.user)
    user = User.objects.get(username=request.GET.get("username", None))

    if bool(request.GET.get("add", None)):
        blacklist.blocked_users.add(user)
        return redirect(reverse(viewname="blacklist_name"))

    blacklist.blocked_users.remove(user)
    return redirect(reverse(viewname="blacklist_name"))
